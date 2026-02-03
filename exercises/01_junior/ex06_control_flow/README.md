# Exercise 06: Control Flow

## Learning Objectives

- Use if/elif/else statements
- Work with for and while loops
- Use break and continue
- Understand loop control

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## If/Elif/Else

```python
def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
```

## For Loops

```python
# Iterate over a list
for item in [1, 2, 3]:
    print(item)

# Iterate with index
for i, item in enumerate([1, 2, 3]):
    print(i, item)

# Range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
```

## While Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Break and Continue

```python
# break - exit the loop
for i in range(10):
    if i == 5:
        break

# continue - skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # prints odd numbers only
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex06_control_flow/ -v
```
