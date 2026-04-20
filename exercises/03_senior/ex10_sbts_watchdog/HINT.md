# Hints for Exercise 10: SBTS Watchdog

## LogMessage.from_json

Wrap everything in a try/except and convert parsing errors to `ValueError`:

```python
@classmethod
def from_json(cls, raw: str) -> "LogMessage":
    try:
        data = json.loads(raw)
        return cls(
            timestamp = data["timestamp"],
            component = data["component"],
            event     = data["event"],
            severity  = data["severity"],
            details   = data["details"],
        )
    except (json.JSONDecodeError, KeyError) as exc:
        raise ValueError(f"Invalid log message: {exc}") from exc
```

---

## SBTSState.is_operational

Three independent conditions joined with `and`:

```python
def is_operational(self) -> bool:
    return (
        self.gps     == GPSState.SYNCED
        and self.ng_link == NGLinkState.CONNECTED
        and self.cell    != CellState.FAULTY
        and self.cell    != CellState.UNKNOWN
    )
```

---

## SBTSWatchdog.process_message

Dispatch to the right handler by `msg.component`:

```python
def process_message(self, raw: str) -> SBTSAlert | None:
    msg = LogMessage.from_json(raw)          # may raise ValueError
    self.message_count += 1

    handlers = {
        "GPS":     self._handle_gps,
        "NG_LINK": self._handle_ng_link,
        "NR_CELL": self._handle_nr_cell,
    }
    handler = handlers.get(msg.component)
    alert = handler(msg) if handler else None

    if alert:
        self.state.record_alert(alert)
        if self.alert_callback:
            self.alert_callback(alert)

    return alert
```

---

## _handle_gps

```python
def _handle_gps(self, msg: LogMessage) -> SBTSAlert | None:
    if msg.event == "SYNC_ACQUIRED":
        self.state.gps = GPSState.SYNCED
        return SBTSAlert(AlertSeverity.INFO, "GPS", msg.event,
                         "GPS synchronisation acquired")
    if msg.event == "SYNC_LOST":
        self.state.gps = GPSState.UNSYNCED
        return SBTSAlert(AlertSeverity.CRITICAL, "GPS", msg.event,
                         "GPS synchronisation LOST — timing unreliable!")
    return None
```

---

## _handle_ng_link

```python
def _handle_ng_link(self, msg: LogMessage) -> SBTSAlert | None:
    amf = msg.details.get("amf_ip", "?")
    if msg.event == "AMF_CONNECTED":
        self.state.ng_link = NGLinkState.CONNECTED
        return SBTSAlert(AlertSeverity.INFO, "NG_LINK", msg.event,
                         f"NG link UP — connected to AMF {amf}")
    if msg.event == "AMF_DISCONNECTED":
        self.state.ng_link = NGLinkState.DISCONNECTED
        return SBTSAlert(AlertSeverity.CRITICAL, "NG_LINK", msg.event,
                         f"NG link DOWN — AMF {amf} unreachable!")
    if msg.event == "AMF_RECONNECTING":
        self.state.ng_link = NGLinkState.RECONNECTING
        return SBTSAlert(AlertSeverity.WARNING, "NG_LINK", msg.event,
                         f"NG link reconnecting to AMF {amf}…")
    return None
```

---

## _handle_nr_cell

```python
def _handle_nr_cell(self, msg: LogMessage) -> SBTSAlert | None:
    new   = msg.details.get("new_state", "UNKNOWN")
    cid   = msg.details.get("cell_id",   "UNKNOWN")

    try:
        self.state.cell = CellState(new)
    except ValueError:
        self.state.cell = CellState.UNKNOWN

    if new == "ON_AIR":
        return SBTSAlert(AlertSeverity.INFO, "NR_CELL", msg.event,
                         f"NR Cell {cid} is now ON AIR — serving UEs")
    if new == "FAULTY":
        return SBTSAlert(AlertSeverity.CRITICAL, "NR_CELL", msg.event,
                         f"NR Cell {cid} entered FAULTY state")
    if new == "LOCKED":
        return SBTSAlert(AlertSeverity.WARNING, "NR_CELL", msg.event,
                         f"NR Cell {cid} is LOCKED (administrative)")
    return None  # IDLE or unknown → no alert
```

---

## check_health

```python
def check_health(self) -> dict:
    critical = sum(
        1 for a in self.state.alert_history
        if a.severity == AlertSeverity.CRITICAL
    )
    return {
        "operational":        self.state.is_operational(),
        "gps":                self.state.gps.value,
        "ng_link":            self.state.ng_link.value,
        "cell":               self.state.cell.value,
        "messages_processed": self.message_count,
        "alerts_total":       len(self.state.alert_history),
        "critical_alerts":    critical,
    }
```

---

## listen_for_logs

Use the socket as a context manager so it closes automatically:

```python
def listen_for_logs(host, port, watchdog, stop_event, buf_size=65535):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.settimeout(0.5)          # allow stop_event check every 0.5 s

        while not stop_event.is_set():
            try:
                data, _ = sock.recvfrom(buf_size)
                watchdog.process_message(data.decode("utf-8"))
            except socket.timeout:
                continue
            except ValueError:
                pass  # malformed datagram — ignore and keep listening
```
