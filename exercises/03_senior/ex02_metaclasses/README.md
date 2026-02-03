# Exercise 02: Metaclasses

## Learning Objectives

- Understand how classes are created
- Create custom metaclasses
- Use `__new__` and `__init__` in metaclasses
- Control class attributes and methods

## Instructions

Fix the metaclasses in `exercise.py` to make all tests pass.

## How Classes Are Created

```python
# When you write:
class MyClass:
    x = 1

# Python essentially does:
MyClass = type('MyClass', (), {'x': 1})
```

## Custom Metaclass

```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Called when class is created
        # Can modify namespace before class exists
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        # Called after class is created
        super().__init__(name, bases, namespace)

class MyClass(metaclass=MyMeta):
    pass
```

## Common Use Cases

- Registering classes automatically
- Enforcing interfaces
- Adding methods/attributes to classes
- Validation of class structure

## Run Tests

```bash
uv run pytest exercises/03_senior/ex02_metaclasses/ -v
```
