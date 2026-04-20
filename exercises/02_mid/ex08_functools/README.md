# Exercise 08: functools

## Learning Objectives

- Use `functools.partial` to create specialized functions
- Use `functools.reduce` to aggregate sequences
- Use `functools.lru_cache` for memoization
- Use `functools.cmp_to_key` for custom sorting

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## Key functools Features

```python
import functools

# partial: fix some arguments of a function
def multiply(x, y): return x * y
double = functools.partial(multiply, 2)
double(5)  # 10

# reduce: apply a function cumulatively
functools.reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10

# lru_cache: memoize function results
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# cmp_to_key: use old-style comparator with sorted()
def cmp(a, b): return (a > b) - (a < b)
sorted(items, key=functools.cmp_to_key(cmp))
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex08_functools/ -v
```
