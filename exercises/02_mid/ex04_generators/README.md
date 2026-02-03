# Exercise 04: Generators

## Learning Objectives

- Create generator functions with yield
- Understand lazy evaluation
- Use generator expressions
- Work with itertools

## Instructions

Fix the generators in `exercise.py` to make all tests pass.

## Generator Functions

```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Usage
for num in count_up(5):
    print(num)  # 0, 1, 2, 3, 4
```

## Generator Expressions

```python
# Like list comprehension but with parentheses
squares = (x**2 for x in range(5))

# Lazy - values computed on demand
for sq in squares:
    print(sq)
```

## Why Generators?

- Memory efficient - don't store all values
- Can represent infinite sequences
- Values computed on demand

## Common Patterns

```python
# Filtering
def even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

# Transforming
def doubled(numbers):
    for n in numbers:
        yield n * 2
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex04_generators/ -v
```
