"""
Tests for Exercise 10: SBTS Watchdog — 5G Base Station Real-Time Monitor

Tests cover:
  - LogMessage parsing (valid JSON, bad JSON, missing keys)
  - SBTSState.is_operational()
  - Each watchdog handler (_handle_gps, _handle_ng_link, _handle_nr_cell)
  - Alert callback firing
  - check_health() dict structure and values
  - listen_for_logs() via a mocked UDP socket
"""

import json
import socket
import threading
from unittest.mock import MagicMock, call, patch

import pytest

from exercise import (
    AlertSeverity,
    CellState,
    GPSState,
    LogMessage,
    NGLinkState,
    SBTSAlert,
    SBTSState,
    SBTSWatchdog,
    listen_for_logs,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def make_raw(component: str, event: str, severity: str = "INFO", **details) -> str:
    return json.dumps({
        "timestamp": "2024-11-01T08:00:00Z",
        "component": component,
        "event":     event,
        "severity":  severity,
        "details":   details,
    })


def gps_acquired()       -> str: return make_raw("GPS",     "SYNC_ACQUIRED",    satellites=8)
def gps_lost()           -> str: return make_raw("GPS",     "SYNC_LOST",        "CRITICAL", satellites=0)
def amf_connected()      -> str: return make_raw("NG_LINK", "AMF_CONNECTED",    amf_ip="10.0.0.1")
def amf_disconnected()   -> str: return make_raw("NG_LINK", "AMF_DISCONNECTED", "CRITICAL", amf_ip="10.0.0.1")
def amf_reconnecting()   -> str: return make_raw("NG_LINK", "AMF_RECONNECTING", "WARNING",  amf_ip="10.0.0.1")
def cell_state(new: str) -> str: return make_raw("NR_CELL", "CELL_STATE_CHANGE", cell_id="NR-001", old_state="IDLE", new_state=new)


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def callback():
    return MagicMock()


@pytest.fixture
def dog(callback):
    return SBTSWatchdog(alert_callback=callback)


@pytest.fixture
def dog_no_cb():
    return SBTSWatchdog()


# ── LogMessage tests ──────────────────────────────────────────────────────────

class TestLogMessage:
    def test_parse_valid(self):
        msg = LogMessage.from_json(gps_acquired())
        assert msg.component == "GPS"
        assert msg.event     == "SYNC_ACQUIRED"
        assert msg.severity  == "INFO"
        assert msg.details   == {"satellites": 8}

    def test_parse_nr_cell(self):
        msg = LogMessage.from_json(cell_state("ON_AIR"))
        assert msg.component == "NR_CELL"
        assert msg.details["new_state"] == "ON_AIR"

    def test_invalid_json_raises_value_error(self):
        with pytest.raises(ValueError):
            LogMessage.from_json("not json {{{")

    def test_missing_key_raises_value_error(self):
        raw = json.dumps({"timestamp": "2024-01-01T00:00:00Z", "component": "GPS"})
        with pytest.raises(ValueError):
            LogMessage.from_json(raw)


# ── SBTSState tests ───────────────────────────────────────────────────────────

class TestSBTSState:
    def test_unknown_is_not_operational(self):
        s = SBTSState()
        assert s.is_operational() is False

    def test_fully_operational(self):
        s = SBTSState()
        s.gps     = GPSState.SYNCED
        s.ng_link = NGLinkState.CONNECTED
        s.cell    = CellState.ON_AIR
        assert s.is_operational() is True

    def test_idle_cell_is_operational(self):
        s = SBTSState()
        s.gps     = GPSState.SYNCED
        s.ng_link = NGLinkState.CONNECTED
        s.cell    = CellState.IDLE
        assert s.is_operational() is True

    @pytest.mark.parametrize("bad_gps", [GPSState.UNKNOWN, GPSState.UNSYNCED])
    def test_bad_gps_not_operational(self, bad_gps):
        s = SBTSState()
        s.gps     = bad_gps
        s.ng_link = NGLinkState.CONNECTED
        s.cell    = CellState.ON_AIR
        assert s.is_operational() is False

    @pytest.mark.parametrize("bad_ng", [NGLinkState.UNKNOWN, NGLinkState.DISCONNECTED, NGLinkState.RECONNECTING])
    def test_bad_ng_link_not_operational(self, bad_ng):
        s = SBTSState()
        s.gps     = GPSState.SYNCED
        s.ng_link = bad_ng
        s.cell    = CellState.ON_AIR
        assert s.is_operational() is False

    def test_faulty_cell_not_operational(self):
        s = SBTSState()
        s.gps     = GPSState.SYNCED
        s.ng_link = NGLinkState.CONNECTED
        s.cell    = CellState.FAULTY
        assert s.is_operational() is False


# ── GPS handler tests ─────────────────────────────────────────────────────────

class TestGPSHandler:
    def test_sync_acquired_sets_state(self, dog):
        dog.process_message(gps_acquired())
        assert dog.state.gps == GPSState.SYNCED

    def test_sync_acquired_produces_info_alert(self, dog, callback):
        alert = dog.process_message(gps_acquired())
        assert alert is not None
        assert alert.severity  == AlertSeverity.INFO
        assert alert.component == "GPS"
        callback.assert_called_once()

    def test_sync_lost_sets_state(self, dog):
        dog.process_message(gps_lost())
        assert dog.state.gps == GPSState.UNSYNCED

    def test_sync_lost_produces_critical_alert(self, dog, callback):
        alert = dog.process_message(gps_lost())
        assert alert is not None
        assert alert.severity == AlertSeverity.CRITICAL
        callback.assert_called_once_with(alert)

    def test_unknown_gps_event_produces_no_alert(self, dog_no_cb):
        raw = make_raw("GPS", "SOME_OTHER_EVENT")
        alert = dog_no_cb.process_message(raw)
        assert alert is None


# ── NG-link handler tests ─────────────────────────────────────────────────────

class TestNGLinkHandler:
    def test_amf_connected(self, dog):
        dog.process_message(amf_connected())
        assert dog.state.ng_link == NGLinkState.CONNECTED

    def test_amf_connected_info_alert(self, dog, callback):
        alert = dog.process_message(amf_connected())
        assert alert.severity == AlertSeverity.INFO

    def test_amf_disconnected(self, dog):
        dog.process_message(amf_disconnected())
        assert dog.state.ng_link == NGLinkState.DISCONNECTED

    def test_amf_disconnected_critical_alert(self, dog, callback):
        alert = dog.process_message(amf_disconnected())
        assert alert.severity == AlertSeverity.CRITICAL
        callback.assert_called_once_with(alert)

    def test_amf_reconnecting(self, dog):
        dog.process_message(amf_reconnecting())
        assert dog.state.ng_link == NGLinkState.RECONNECTING

    def test_amf_reconnecting_warning_alert(self, dog, callback):
        alert = dog.process_message(amf_reconnecting())
        assert alert.severity == AlertSeverity.WARNING


# ── NR Cell handler tests ─────────────────────────────────────────────────────

class TestNRCellHandler:
    @pytest.mark.parametrize("new_state,expected_cell,expected_severity", [
        ("ON_AIR", CellState.ON_AIR, AlertSeverity.INFO),
        ("FAULTY", CellState.FAULTY, AlertSeverity.CRITICAL),
        ("LOCKED", CellState.LOCKED, AlertSeverity.WARNING),
    ])
    def test_cell_state_alerts(self, dog, callback, new_state, expected_cell, expected_severity):
        alert = dog.process_message(cell_state(new_state))
        assert dog.state.cell   == expected_cell
        assert alert is not None
        assert alert.severity   == expected_severity

    def test_cell_idle_no_alert(self, dog_no_cb):
        alert = dog_no_cb.process_message(cell_state("IDLE"))
        assert dog_no_cb.state.cell == CellState.IDLE
        assert alert is None

    def test_faulty_alert_message_contains_cell_id(self, dog):
        alert = dog.process_message(cell_state("FAULTY"))
        assert "NR-001" in alert.message

    def test_on_air_alert_message_mentions_on_air(self, dog):
        alert = dog.process_message(cell_state("ON_AIR"))
        assert "ON AIR" in alert.message or "ON_AIR" in alert.message or "serving" in alert.message.lower()


# ── process_message orchestration tests ───────────────────────────────────────

class TestProcessMessage:
    def test_message_count_increments(self, dog):
        dog.process_message(gps_acquired())
        dog.process_message(amf_connected())
        assert dog.message_count == 2

    def test_alert_recorded_in_history(self, dog):
        dog.process_message(gps_lost())
        assert len(dog.state.alert_history) == 1
        assert dog.state.alert_history[0].severity == AlertSeverity.CRITICAL

    def test_no_callback_no_error(self, dog_no_cb):
        # Should not raise even without a callback
        dog_no_cb.process_message(gps_lost())

    def test_bad_json_raises_value_error(self, dog):
        with pytest.raises(ValueError):
            dog.process_message("garbage")

    def test_callback_called_for_each_alert(self, dog, callback):
        dog.process_message(gps_lost())
        dog.process_message(amf_disconnected())
        assert callback.call_count == 2

    def test_no_alert_no_callback(self, dog, callback):
        dog.process_message(cell_state("IDLE"))
        callback.assert_not_called()


# ── check_health tests ────────────────────────────────────────────────────────

class TestCheckHealth:
    def test_returns_dict_with_all_keys(self, dog):
        health = dog.check_health()
        expected_keys = {
            "operational", "gps", "ng_link", "cell",
            "messages_processed", "alerts_total", "critical_alerts",
        }
        assert expected_keys == set(health.keys())

    def test_initial_state_not_operational(self, dog):
        health = dog.check_health()
        assert health["operational"] is False
        assert health["gps"]     == "UNKNOWN"
        assert health["ng_link"] == "UNKNOWN"
        assert health["cell"]    == "UNKNOWN"

    def test_fully_operational_after_good_messages(self, dog):
        dog.process_message(gps_acquired())
        dog.process_message(amf_connected())
        dog.process_message(cell_state("ON_AIR"))
        health = dog.check_health()
        assert health["operational"] is True
        assert health["gps"]     == "SYNCED"
        assert health["ng_link"] == "CONNECTED"
        assert health["cell"]    == "ON_AIR"

    def test_alert_counts(self, dog):
        dog.process_message(gps_acquired())    # INFO
        dog.process_message(gps_lost())        # CRITICAL
        dog.process_message(amf_disconnected()) # CRITICAL
        health = dog.check_health()
        assert health["alerts_total"]    == 3
        assert health["critical_alerts"] == 2
        assert health["messages_processed"] == 3


# ── listen_for_logs tests (mocked UDP socket) ─────────────────────────────────

class TestListenForLogs:
    """Simulate tshark-like packet capture by mocking socket.socket."""

    def test_listen_processes_messages(self):
        """Messages received from the UDP socket are forwarded to the watchdog."""
        stop = threading.Event()
        dog  = SBTSWatchdog()

        payloads = [
            gps_acquired().encode(),
            amf_connected().encode(),
            cell_state("ON_AIR").encode(),
        ]

        # Mock socket that returns our payloads then sets stop_event
        mock_sock = MagicMock()

        call_count = [0]

        def fake_recv(size):
            i = call_count[0]
            call_count[0] += 1
            if i < len(payloads):
                return payloads[i]
            stop.set()
            raise socket.timeout

        mock_sock.recvfrom.side_effect = lambda size: (fake_recv(size), ("10.0.0.1", 4200))

        with patch("exercise.socket.socket") as mock_socket_cls:
            instance = mock_socket_cls.return_value.__enter__.return_value
            instance.recvfrom.side_effect = mock_sock.recvfrom.side_effect

            # Run listen_for_logs in a thread so it doesn't block the test
            t = threading.Thread(
                target=listen_for_logs,
                args=("0.0.0.0", 4200, dog, stop),
                daemon=True,
            )
            t.start()
            t.join(timeout=3.0)

        assert dog.message_count == 3
        assert dog.state.gps     == GPSState.SYNCED
        assert dog.state.ng_link == NGLinkState.CONNECTED
        assert dog.state.cell    == CellState.ON_AIR

    def test_listen_binds_to_correct_address(self):
        """The socket must be bound to the given host and port."""
        stop = threading.Event()
        stop.set()  # stop immediately

        with patch("exercise.socket.socket") as mock_socket_cls:
            instance = mock_socket_cls.return_value.__enter__.return_value
            instance.recvfrom.side_effect = socket.timeout

            listen_for_logs("0.0.0.0", 4200, SBTSWatchdog(), stop)

            instance.bind.assert_called_once_with(("0.0.0.0", 4200))

    def test_listen_sets_socket_options(self):
        """SO_REUSEADDR and a timeout must be configured."""
        stop = threading.Event()
        stop.set()

        with patch("exercise.socket.socket") as mock_socket_cls:
            instance = mock_socket_cls.return_value.__enter__.return_value
            instance.recvfrom.side_effect = socket.timeout

            listen_for_logs("0.0.0.0", 4200, SBTSWatchdog(), stop)

            instance.setsockopt.assert_called_once_with(
                socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
            )
            instance.settimeout.assert_called_once()
