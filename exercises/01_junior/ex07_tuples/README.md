# Exercise 07: Tuples

## Learning Objectives

- Understand tuples and their immutability
- Learn tuple indexing, unpacking, and concatenation
- Convert between tuples and lists

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

Each function has a `TODO` comment explaining what needs to be done.

## Tuples in Python

```python
# Create a tuple
point = (1, 2, 3)

# Indexing
first = point[0]   # 1
last = point[-1]   # 3

# Unpacking
x, y, z = point

# Concatenation
combined = (1, 2) + (3, 4)  # (1, 2, 3, 4)

# Count occurrences
count = (1, 2, 2, 3).count(2)  # 2

# Convert to list and back
as_list = list(point)
as_list.append(4)
back = tuple(as_list)
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex07_tuples/ -v
```
