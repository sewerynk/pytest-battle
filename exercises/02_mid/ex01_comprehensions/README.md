# Exercise 01: Comprehensions

## Learning Objectives

- Master list comprehensions
- Learn dictionary comprehensions
- Understand set comprehensions
- Use conditional comprehensions

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# With transformation
upper = [s.upper() for s in ["a", "b", "c"]]  # ["A", "B", "C"]
```

## Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}  # {"a": 1, "b": 2, "c": 3}
```

## Set Comprehensions

```python
unique_lengths = {len(word) for word in ["hello", "world", "hi"]}
# {2, 5}
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex01_comprehensions/ -v
```
