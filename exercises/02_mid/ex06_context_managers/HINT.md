# Hints for Exercise 06

## Hint 1: Timer Class

```python
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        return False
```

## Hint 2: SuppressErrors

```python
class SuppressErrors:
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return exc_type in self.exception_types
        return False
```

## Hint 3: Counter

```python
class Counter:
    count = 0

    def __enter__(self):
        Counter.count += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
```

## Hint 4: temporary_value

```python
@contextmanager
def temporary_value(obj, key, value):
    had_key = key in obj
    old_value = obj.get(key)

    obj[key] = value
    try:
        yield obj
    finally:
        if had_key:
            obj[key] = old_value
        else:
            del obj[key]
```

## Hint 5: capture_output

```python
@contextmanager
def capture_output():
    output = []
    yield output
```

## Hint 6: transaction

```python
@contextmanager
def transaction(data):
    backup = data.copy()
    try:
        yield data
    except Exception:
        data.clear()
        data.update(backup)
        raise
```
