# Hints for Exercise 03

## Hint 1: Lazy Descriptor

```python
class Lazy:
    def __init__(self, func):
        self.func = func
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.name not in obj.__dict__:
            obj.__dict__[self.name] = self.func(obj)
        return obj.__dict__[self.name]
```

## Hint 2: TypedAttribute

```python
class TypedAttribute:
    def __init__(self, expected_type, default=None):
        self.expected_type = expected_type
        self.default = default
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, self.default)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type.__name__}")
        obj.__dict__[self.name] = value
```

## Hint 3: BoundedNumber

```python
class BoundedNumber:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.name = None

    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        obj.__dict__[self.name] = value
```

## Hint 4: Observable

```python
class Observable:
    def __init__(self):
        self.name = None
        self.observers = []

    def __set__(self, obj, value):
        old_value = obj.__dict__.get(self.name)
        obj.__dict__[self.name] = value
        for callback in self.observers:
            callback(obj, old_value, value)

    def add_observer(self, callback):
        self.observers.append(callback)
```

## Hint 5: CachedProperty

```python
class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.name = None
        self.__doc__ = func.__doc__

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.name not in obj.__dict__:
            obj.__dict__[self.name] = self.func(obj)
        return obj.__dict__[self.name]
```
