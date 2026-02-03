# Exercise 03: Decorators

## Learning Objectives

- Understand function decorators
- Create simple decorators
- Use functools.wraps
- Create decorators with arguments

## Instructions

Fix the decorators in `exercise.py` to make all tests pass.

## Decorator Basics

A decorator is a function that wraps another function:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"
```

## Using functools.wraps

Preserve the original function's metadata:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Decorators with Arguments

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex03_decorators/ -v
```
