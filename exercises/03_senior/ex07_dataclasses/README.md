# Exercise 07: Dataclasses

## Learning Objectives

- Use `@dataclass` to auto-generate `__init__`, `__repr__`, `__eq__`
- Use `frozen=True` for immutable dataclasses (hashable)
- Use `order=True` for comparison operators
- Use `field(default_factory=...)` for mutable defaults
- Add class variables and methods to dataclasses

## Instructions

Fix the classes in `exercise.py` to make all tests pass.

## Dataclasses in Python

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

# Auto-generated: __init__, __repr__, __eq__
p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
p1 == p2  # True

# Frozen (immutable + hashable)
@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float

# Orderable
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

# Mutable default (use field!)
@dataclass
class Container:
    items: list = field(default_factory=list)

# Class variable (not a field)
from typing import ClassVar

@dataclass
class Student:
    name: str
    school: ClassVar[str] = "Python Academy"
```

## Run Tests

```bash
uv run pytest exercises/03_senior/ex07_dataclasses/ -v
```
