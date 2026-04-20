# Hints for Exercise 08: Threading

## run_in_thread
```python
t = threading.Thread(target=func, args=args, daemon=True)
t.start()
return t
```

## SafeCounter
```python
def __init__(self):
    self.value = 0
    self._lock = threading.Lock()

def increment(self):
    with self._lock:
        self.value += 1

def get(self):
    return self.value
```

## EventSignal
```python
def __init__(self):
    self.event = threading.Event()

def signal(self):
    self.event.set()

def wait_for_signal(self, timeout):
    return self.event.wait(timeout=timeout)
```

## parallel_map
```python
results = [None] * len(items)

def worker(i, item):
    results[i] = func(item)

threads = [threading.Thread(target=worker, args=(i, item)) for i, item in enumerate(items)]
for t in threads:
    t.start()
for t in threads:
    t.join()
return results
```
