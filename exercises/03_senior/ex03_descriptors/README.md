# Exercise 03: Descriptors

## Learning Objectives

- Understand the descriptor protocol
- Create data and non-data descriptors
- Implement lazy evaluation
- Build validated attributes

## Instructions

Fix the descriptors in `exercise.py` to make all tests pass.

## Descriptor Protocol

```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        # Called when attribute is accessed
        pass

    def __set__(self, obj, value):
        # Called when attribute is set
        pass

    def __delete__(self, obj):
        # Called when attribute is deleted
        pass
```

## Data vs Non-Data Descriptors

- **Data descriptor**: Has `__get__` AND `__set__` (or `__delete__`)
- **Non-data descriptor**: Has only `__get__`

Data descriptors take precedence over instance `__dict__`.

## Example: Validated Attribute

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Must be positive")
        obj.__dict__[self.name] = value
```

## Run Tests

```bash
uv run pytest exercises/03_senior/ex03_descriptors/ -v
```
