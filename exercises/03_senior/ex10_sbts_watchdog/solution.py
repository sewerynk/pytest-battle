"""
Reference solution for Exercise 10: SBTS Watchdog

This file is intentionally separate from exercise.py so you can compare
your implementation without accidentally copying it first.

Read it only after you have made all tests pass on your own!
"""

import json
import socket
import threading
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Callable


# ── State enumerations ────────────────────────────────────────────────────────

class GPSState(Enum):
    UNKNOWN  = "UNKNOWN"
    SYNCED   = "SYNCED"
    UNSYNCED = "UNSYNCED"


class NGLinkState(Enum):
    UNKNOWN      = "UNKNOWN"
    CONNECTED    = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    RECONNECTING = "RECONNECTING"


class CellState(Enum):
    UNKNOWN = "UNKNOWN"
    IDLE    = "IDLE"
    ON_AIR  = "ON_AIR"
    LOCKED  = "LOCKED"
    FAULTY  = "FAULTY"


class AlertSeverity(Enum):
    INFO     = "INFO"
    WARNING  = "WARNING"
    CRITICAL = "CRITICAL"


# ── Data classes ──────────────────────────────────────────────────────────────

@dataclass
class LogMessage:
    timestamp: str
    component: str
    event:     str
    severity:  str
    details:   dict

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


@dataclass
class SBTSAlert:
    severity:  AlertSeverity
    component: str
    event:     str
    message:   str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")


# ── Station state tracker ─────────────────────────────────────────────────────

class SBTSState:
    def __init__(self) -> None:
        self.gps:           GPSState    = GPSState.UNKNOWN
        self.ng_link:       NGLinkState = NGLinkState.UNKNOWN
        self.cell:          CellState   = CellState.UNKNOWN
        self.alert_history: list[SBTSAlert] = []

    def is_operational(self) -> bool:
        return (
            self.gps     == GPSState.SYNCED
            and self.ng_link == NGLinkState.CONNECTED
            and self.cell    not in (CellState.FAULTY, CellState.UNKNOWN)
        )

    def record_alert(self, alert: SBTSAlert) -> None:
        self.alert_history.append(alert)


# ── Watchdog ──────────────────────────────────────────────────────────────────

class SBTSWatchdog:
    def __init__(self, alert_callback: Callable[[SBTSAlert], None] | None = None) -> None:
        self.state          = SBTSState()
        self.alert_callback = alert_callback
        self.message_count  = 0

    def process_message(self, raw: str) -> SBTSAlert | None:
        msg = LogMessage.from_json(raw)   # raises ValueError on bad input
        self.message_count += 1

        handlers = {
            "GPS":     self._handle_gps,
            "NG_LINK": self._handle_ng_link,
            "NR_CELL": self._handle_nr_cell,
        }
        handler = handlers.get(msg.component)
        alert   = handler(msg) if handler else None

        if alert:
            self.state.record_alert(alert)
            if self.alert_callback:
                self.alert_callback(alert)

        return alert

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

    # ── handlers ──────────────────────────────────────────────────────────────

    def _handle_gps(self, msg: LogMessage) -> SBTSAlert | None:
        if msg.event == "SYNC_ACQUIRED":
            self.state.gps = GPSState.SYNCED
            return SBTSAlert(
                AlertSeverity.INFO, "GPS", msg.event,
                "GPS synchronisation acquired",
            )
        if msg.event == "SYNC_LOST":
            self.state.gps = GPSState.UNSYNCED
            return SBTSAlert(
                AlertSeverity.CRITICAL, "GPS", msg.event,
                "GPS synchronisation LOST — timing unreliable!",
            )
        return None

    def _handle_ng_link(self, msg: LogMessage) -> SBTSAlert | None:
        amf = msg.details.get("amf_ip", "?")

        if msg.event == "AMF_CONNECTED":
            self.state.ng_link = NGLinkState.CONNECTED
            return SBTSAlert(
                AlertSeverity.INFO, "NG_LINK", msg.event,
                f"NG link UP — connected to AMF {amf}",
            )
        if msg.event == "AMF_DISCONNECTED":
            self.state.ng_link = NGLinkState.DISCONNECTED
            return SBTSAlert(
                AlertSeverity.CRITICAL, "NG_LINK", msg.event,
                f"NG link DOWN — AMF {amf} unreachable!",
            )
        if msg.event == "AMF_RECONNECTING":
            self.state.ng_link = NGLinkState.RECONNECTING
            return SBTSAlert(
                AlertSeverity.WARNING, "NG_LINK", msg.event,
                f"NG link reconnecting to AMF {amf}…",
            )
        return None

    def _handle_nr_cell(self, msg: LogMessage) -> SBTSAlert | None:
        new = msg.details.get("new_state", "UNKNOWN")
        cid = msg.details.get("cell_id",   "UNKNOWN")

        try:
            self.state.cell = CellState(new)
        except ValueError:
            self.state.cell = CellState.UNKNOWN

        if new == "ON_AIR":
            return SBTSAlert(
                AlertSeverity.INFO, "NR_CELL", msg.event,
                f"NR Cell {cid} is now ON AIR — serving UEs",
            )
        if new == "FAULTY":
            return SBTSAlert(
                AlertSeverity.CRITICAL, "NR_CELL", msg.event,
                f"NR Cell {cid} entered FAULTY state",
            )
        if new == "LOCKED":
            return SBTSAlert(
                AlertSeverity.WARNING, "NR_CELL", msg.event,
                f"NR Cell {cid} is LOCKED (administrative)",
            )
        return None  # IDLE → normal standby, no alert needed


# ── UDP listener ──────────────────────────────────────────────────────────────

def listen_for_logs(
    host:        str,
    port:        int,
    watchdog:    SBTSWatchdog,
    stop_event:  threading.Event,
    buf_size:    int = 65535,
) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.settimeout(0.5)        # check stop_event every 0.5 s

        while not stop_event.is_set():
            try:
                data, _ = sock.recvfrom(buf_size)
                watchdog.process_message(data.decode("utf-8"))
            except socket.timeout:
                continue            # no datagram — check stop_event and retry
            except ValueError:
                pass                # malformed datagram — ignore, keep running
