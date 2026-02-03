# Exercise 06: Context Managers

## Learning Objectives

- Understand the `with` statement
- Create context managers using classes
- Use `contextlib` decorators
- Handle resource cleanup

## Instructions

Fix the context managers in `exercise.py` to make all tests pass.

## The `with` Statement

```python
with open("file.txt") as f:
    content = f.read()
# File is automatically closed
```

## Class-Based Context Manager

```python
class MyContext:
    def __enter__(self):
        print("Entering")
        return self  # Value available as 'x' in 'as x'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
        return False  # Don't suppress exceptions
```

## Using contextlib

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Before")
    try:
        yield "value"  # This is the 'as' value
    finally:
        print("After")
```

## Exception Handling

In `__exit__`:
- Return `True` to suppress the exception
- Return `False` to let it propagate

## Run Tests

```bash
uv run pytest exercises/02_mid/ex06_context_managers/ -v
```
