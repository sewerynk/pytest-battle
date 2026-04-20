# Exercise 10: SBTS Watchdog — 5G Base Station Real-Time Monitor

> **Difficulty:** ★★★★★  Expert
> **Topics:** dataclasses, enums, threading, mocking, real-time stream processing

---

## Story

You are a Python developer at a telecom operator running a 5G SA (Standalone)
network.  Your fleet of SBTS (Small Base Transceiver Stations) streams
operational log messages over UDP to a central monitoring host on **port 4200**.
In the field the packets are captured with **tshark** and decoded as UTF-8 JSON
lines, one message per UDP datagram.

Each message describes one state change inside the SBTS:

| Component  | Events                                              |
|------------|-----------------------------------------------------|
| `GPS`      | `SYNC_ACQUIRED`, `SYNC_LOST`                        |
| `NG_LINK`  | `AMF_CONNECTED`, `AMF_DISCONNECTED`, `AMF_RECONNECTING` |
| `NR_CELL`  | `CELL_STATE_CHANGE` (with `new_state` in details)   |

Example log line (one UDP payload):

```json
{
  "timestamp": "2024-11-01T08:23:45Z",
  "component": "NR_CELL",
  "event":     "CELL_STATE_CHANGE",
  "severity":  "INFO",
  "details":   {"cell_id": "NR-001", "old_state": "IDLE", "new_state": "ON_AIR"}
}
```

Your task is to build a **`SBTSWatchdog`** that:

1. Parses each raw JSON line into a `LogMessage`
2. Updates the tracked `SBTSState` (GPS / NG-link / cell)
3. Fires a user-supplied `alert_callback(SBTSAlert)` whenever something critical
   happens — GPS sync lost, AMF disconnected, cell goes FAULTY, etc.
4. Exposes a `check_health()` method that returns a summary dict
5. Can be wired to a real UDP socket via `listen_for_logs()` (the streaming
   entry-point, simulated in tests via a mock socket)

---

## Architecture

```
UDP port 4200                SBTSWatchdog
   │                             │
   │  raw JSON bytes             │
   └──► listen_for_logs() ──────►│
                                 │ process_message(raw)
                                 │   ├─ LogMessage.from_json()
                                 │   ├─ _handle_gps()
                                 │   ├─ _handle_ng_link()
                                 │   └─ _handle_nr_cell()
                                 │         └─ alert_callback(SBTSAlert)  ◄── your code calls this
                                 │
                                 └─ check_health() → dict
```

---

## What you must implement

Open `exercise.py`.  Every method marked `# TODO` needs a real body.

| Class / function     | What to do                                              |
|----------------------|---------------------------------------------------------|
| `LogMessage.from_json` | Parse raw JSON string into a `LogMessage` instance   |
| `SBTSState.is_operational` | Return `True` only when GPS synced + NG link up + cell not FAULTY |
| `SBTSWatchdog.process_message` | Orchestrate parsing → handler → alert            |
| `SBTSWatchdog._handle_gps` | Update GPS state, return `SBTSAlert` on `SYNC_LOST` |
| `SBTSWatchdog._handle_ng_link` | Update NG state, return alert on disconnect/reconnect |
| `SBTSWatchdog._handle_nr_cell` | Update cell state, return alert for FAULTY / ON_AIR / LOCKED |
| `SBTSWatchdog.check_health` | Return health summary dict (see docstring)          |
| `listen_for_logs`    | Bind a UDP socket, loop-receive, decode, call `process_message` |

---

## Alert severity rules

| Condition                        | Severity   |
|----------------------------------|------------|
| GPS `SYNC_LOST`                  | CRITICAL   |
| GPS `SYNC_ACQUIRED`              | INFO       |
| NG_LINK `AMF_DISCONNECTED`       | CRITICAL   |
| NG_LINK `AMF_RECONNECTING`       | WARNING    |
| NG_LINK `AMF_CONNECTED`          | INFO       |
| NR_CELL new_state = `FAULTY`     | CRITICAL   |
| NR_CELL new_state = `LOCKED`     | WARNING    |
| NR_CELL new_state = `ON_AIR`     | INFO       |
| NR_CELL new_state = `IDLE`       | *(no alert)* |

---

## Run Tests

```bash
uv run pytest exercises/03_senior/ex10_sbts_watchdog/ -v
```

Check the reference implementation after you are done:

```bash
cat exercises/03_senior/ex10_sbts_watchdog/solution.py
```
