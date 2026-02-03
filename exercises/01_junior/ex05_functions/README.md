# Exercise 05: Functions

## Learning Objectives

- Define functions with parameters
- Understand return values
- Use default arguments
- Work with *args and **kwargs

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## Function Basics

```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
result = greet("Alice")  # "Hello, Alice!"
```

## Default Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")           # "Hello, Alice!"
greet("Alice", "Hi")     # "Hi, Alice!"
```

## Multiple Return Values

```python
def get_stats(numbers):
    return min(numbers), max(numbers)

low, high = get_stats([1, 5, 3])  # low=1, high=5
```

## *args and **kwargs

```python
def add_all(*args):
    return sum(args)

add_all(1, 2, 3)  # 6

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex05_functions/ -v
```
