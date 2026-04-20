# Exercise 08: Threading

## Learning Objectives

- Create and start threads with `threading.Thread`
- Use `threading.Lock` for mutual exclusion
- Use `threading.Event` for signalling between threads
- Run tasks in parallel and collect results

## Instructions

Fix the functions and classes in `exercise.py` to make all tests pass.

## Threading Basics

```python
import threading

# Create and start a thread
def worker(x):
    print(x)

t = threading.Thread(target=worker, args=(42,), daemon=True)
t.start()
t.join()  # Wait for thread to finish

# Lock for mutual exclusion
lock = threading.Lock()
with lock:
    shared_value += 1

# Event for signalling
event = threading.Event()
event.set()                       # Signal
event.wait(timeout=1.0)          # Wait (returns True/False)
event.is_set()                   # Check if set
```

## Run Tests

```bash
uv run pytest exercises/03_senior/ex08_threading/ -v
```
