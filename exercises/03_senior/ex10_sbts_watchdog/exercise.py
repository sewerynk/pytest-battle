"""
Exercise 10: SBTS Watchdog — 5G Base Station Real-Time Monitor

A fleet of Small Base Transceiver Stations (SBTS) streams operational logs
over UDP (port 4200).  Your watchdog must parse those logs, track station
state, and fire alerts when critical conditions arise.

Implement every method marked with TODO.
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
    UNKNOWN      = "UNKNOWN"
    SYNCED       = "SYNCED"
    UNSYNCED     = "UNSYNCED"


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
    """A single operational log line received from the SBTS."""
    timestamp: str
    component: str   # "GPS" | "NG_LINK" | "NR_CELL"
    event: str
    severity: str
    details: dict

    @classmethod
    def from_json(cls, raw: str) -> "LogMessage":
        """Parse a raw JSON string into a LogMessage.

        Args:
            raw: A UTF-8 JSON string with keys:
                 timestamp, component, event, severity, details

        Returns:
            A LogMessage instance.

        Raises:
            ValueError: if the JSON is invalid or required keys are missing.
        """
        # TODO: parse raw with json.loads(), extract the five fields,
        #       and return cls(timestamp=..., component=..., ...)
        #       Wrap json.JSONDecodeError / KeyError in ValueError.
        pass


@dataclass
class SBTSAlert:
    """An alert produced by the watchdog."""
    severity:  AlertSeverity
    component: str
    event:     str
    message:   str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")


# ── Station state tracker ─────────────────────────────────────────────────────

class SBTSState:
    """Mutable snapshot of the current SBTS health."""

    def __init__(self) -> None:
        self.gps:           GPSState   = GPSState.UNKNOWN
        self.ng_link:       NGLinkState = NGLinkState.UNKNOWN
        self.cell:          CellState  = CellState.UNKNOWN
        self.alert_history: list[SBTSAlert] = []

    def is_operational(self) -> bool:
        """Return True when the station is fully operational.

        A station is operational when ALL of the following hold:
          - GPS is SYNCED
          - NG link is CONNECTED
          - Cell is not FAULTY (ON_AIR or IDLE are both acceptable)
        """
        # TODO: implement the three conditions above
        pass

    def record_alert(self, alert: SBTSAlert) -> None:
        """Append alert to alert_history."""
        self.alert_history.append(alert)


# ── Watchdog ──────────────────────────────────────────────────────────────────

class SBTSWatchdog:
    """Real-time watchdog for an SBTS log stream.

    Usage::

        def my_callback(alert: SBTSAlert) -> None:
            print(f"[{alert.severity.value}] {alert.message}")

        dog = SBTSWatchdog(alert_callback=my_callback)
        dog.process_message(raw_json_line)
        health = dog.check_health()
    """

    def __init__(self, alert_callback: Callable[[SBTSAlert], None] | None = None) -> None:
        self.state          = SBTSState()
        self.alert_callback = alert_callback
        self.message_count  = 0

    # ── public API ────────────────────────────────────────────────────────────

    def process_message(self, raw: str) -> SBTSAlert | None:
        """Parse one raw log line, update state, and fire an alert if needed.

        Args:
            raw: A raw UTF-8 JSON log line.

        Returns:
            The SBTSAlert that was produced, or None if no alert was needed.

        Steps:
          1. Parse raw → LogMessage (raise ValueError on bad JSON).
          2. Increment self.message_count.
          3. Dispatch to the right handler (_handle_gps / _handle_ng_link /
             _handle_nr_cell) based on msg.component.
          4. If the handler returns an alert, record it in state.alert_history
             and call self.alert_callback(alert) if one was provided.
          5. Return the alert (or None).
        """
        # TODO: implement the five steps described above
        pass

    def check_health(self) -> dict:
        """Return a snapshot of the current station health.

        Returns a dict with exactly these keys::

            {
                "operational":     bool,          # SBTSState.is_operational()
                "gps":             str,           # GPSState value, e.g. "SYNCED"
                "ng_link":         str,           # NGLinkState value
                "cell":            str,           # CellState value
                "messages_processed": int,        # total messages seen
                "alerts_total":    int,           # len(state.alert_history)
                "critical_alerts": int,           # count with severity CRITICAL
            }
        """
        # TODO: build and return the dict described above
        pass

    # ── private handlers ──────────────────────────────────────────────────────

    def _handle_gps(self, msg: LogMessage) -> SBTSAlert | None:
        """Update GPS state and return an alert when appropriate.

        Events:
          - SYNC_ACQUIRED → set gps to SYNCED,  return INFO alert
          - SYNC_LOST     → set gps to UNSYNCED, return CRITICAL alert
          - anything else → update nothing, return None
        """
        # TODO
        pass

    def _handle_ng_link(self, msg: LogMessage) -> SBTSAlert | None:
        """Update NG-link state and return an alert when appropriate.

        Events:
          - AMF_CONNECTED    → CONNECTED,    INFO alert
          - AMF_DISCONNECTED → DISCONNECTED, CRITICAL alert
          - AMF_RECONNECTING → RECONNECTING, WARNING alert
          - anything else    → None
        """
        # TODO
        pass

    def _handle_nr_cell(self, msg: LogMessage) -> SBTSAlert | None:
        """Update cell state and return an alert when appropriate.

        The event is always CELL_STATE_CHANGE.
        Read new_state from msg.details["new_state"].

        State transitions and alerts:
          - ON_AIR → INFO    "NR Cell {cell_id} is now ON AIR — serving UEs"
          - FAULTY → CRITICAL "NR Cell {cell_id} entered FAULTY state"
          - LOCKED → WARNING  "NR Cell {cell_id} is LOCKED (administrative)"
          - IDLE   → no alert (normal standby)

        Use msg.details.get("cell_id", "UNKNOWN") for cell_id.
        """
        # TODO
        pass


# ── UDP listener (bonus / integration) ───────────────────────────────────────

def listen_for_logs(
    host: str,
    port: int,
    watchdog: SBTSWatchdog,
    stop_event: threading.Event,
    buf_size: int = 65535,
) -> None:
    """Bind a UDP socket and feed received datagrams to the watchdog.

    This function blocks until stop_event is set.

    Args:
        host:       IP address to bind (e.g. "0.0.0.0").
        port:       UDP port to listen on (e.g. 4200).
        watchdog:   The SBTSWatchdog instance to feed messages to.
        stop_event: A threading.Event; when set the function returns cleanly.
        buf_size:   Receive buffer size in bytes.

    Steps:
      1. Create a UDP socket (socket.AF_INET, socket.SOCK_DGRAM).
      2. Set SO_REUSEADDR.
      3. Bind to (host, port).
      4. Set a short socket timeout (e.g. 0.5 s) so the stop_event can be
         checked every iteration.
      5. Loop: recv → decode UTF-8 → watchdog.process_message().
         Ignore socket.timeout.  On stop_event.is_set() break and close.
    """
    # TODO: implement the five steps above
    pass
