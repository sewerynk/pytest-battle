# Hints for Exercise 09: Advanced pytest Patterns

## NotificationService.notify
```python
def notify(self, user_email, message):
    success = self.sender.send(user_email, "Notification", message)
    if success:
        self.sent_count += 1
        return True
    return False
```

## DataProcessor.process_all
```python
def process_all(self, items):
    return [self.transform(item) for item in items]
```

## DataProcessor.process_with_fallback
```python
def process_with_fallback(self, item, fallback):
    try:
        return self.transform(item)
    except Exception:
        return fallback
```

## Cache.get
```python
def get(self, key, default=None):
    if key in self._store:
        self.hits += 1
        return self._store[key]
    self.misses += 1
    return default
```

## Cache.set
```python
def set(self, key, value):
    self._store[key] = value
```

## Cache.clear
```python
def clear(self):
    self._store.clear()
    self.hits = 0
    self.misses = 0
```
