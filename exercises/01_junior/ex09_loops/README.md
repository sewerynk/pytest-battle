# Exercise 09: Loops

## Learning Objectives

- Use `for` loops with `range()` and iterables
- Use `while` loops with conditions
- Break out of loops early with `return`
- Work with nested loops

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

Each function has a `TODO` comment explaining what needs to be done.

## Loops in Python

```python
# for loop with range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# for loop over list
for item in [1, 2, 3]:
    print(item)

# while loop
n = 5
while n > 0:
    print(n)
    n -= 1

# nested loops
for row in [[1, 2], [3, 4]]:
    for item in row:
        print(item)
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex09_loops/ -v
```
