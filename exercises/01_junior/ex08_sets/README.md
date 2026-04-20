# Exercise 08: Sets

## Learning Objectives

- Understand Python sets and their uniqueness property
- Learn set operations: union, intersection, difference
- Use sets to remove duplicates from lists

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

Each function has a `TODO` comment explaining what needs to be done.

## Sets in Python

```python
# Create a set
s = {1, 2, 3}

# Add element
s.add(4)

# Remove duplicates from list
unique = list(set([1, 2, 2, 3]))

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}

union = a | b          # {1, 2, 3, 4}
intersection = a & b   # {2, 3}
difference = a - b     # {1}

# Subset check
{1, 2}.issubset({1, 2, 3})  # True
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex08_sets/ -v
```
