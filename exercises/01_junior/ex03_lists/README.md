# Exercise 03: Lists

## Learning Objectives

- Create and manipulate Python lists
- Understand list methods (append, remove, etc.)
- Use list slicing and indexing

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## List Basics

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
empty = []
```

## List Methods

```python
fruits = ["apple", "banana"]

fruits.append("cherry")      # Add to end
fruits.insert(0, "apricot")  # Insert at index
fruits.remove("banana")      # Remove first occurrence
fruits.pop()                 # Remove and return last
fruits.pop(0)                # Remove and return at index

len(fruits)                  # Length
fruits.index("apple")        # Find index
"apple" in fruits            # Check membership
```

## List Slicing

```python
nums = [0, 1, 2, 3, 4, 5]

nums[0]      # 0 (first)
nums[-1]     # 5 (last)
nums[1:4]    # [1, 2, 3]
nums[:3]     # [0, 1, 2]
nums[3:]     # [3, 4, 5]
nums[::-1]   # [5, 4, 3, 2, 1, 0] (reversed)
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex03_lists/ -v
```
