# Exercise 09: Type Hints and Annotations

## Learning Objectives

- Understand Python type hints and their syntax
- Use `TypeVar` for generic functions
- Use `Callable`, `list[T]`, `dict`, `T | None` annotations
- Write functions that work correctly with typed signatures

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## Type Hints in Python

```python
from typing import TypeVar, Callable, Any

T = TypeVar("T")

# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}"

# Generic function with TypeVar
def identity(x: T) -> T:
    return x

# Callable type
def apply(f: Callable[[int], int], x: int) -> int:
    return f(x)

# Optional / union
def maybe(x: int | None) -> int:
    return x if x is not None else 0

# Filter by type with isinstance
[x for x in items if isinstance(x, int)]
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex09_typing/ -v
```
