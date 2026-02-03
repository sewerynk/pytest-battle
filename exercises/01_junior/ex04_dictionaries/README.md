# Exercise 04: Dictionaries

## Learning Objectives

- Create and manipulate Python dictionaries
- Access, add, and remove key-value pairs
- Iterate over dictionaries

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## Dictionary Basics

```python
# Creating dictionaries
person = {"name": "Alice", "age": 25}
empty = {}

# Access values
person["name"]       # "Alice"
person.get("name")   # "Alice"
person.get("city", "Unknown")  # "Unknown" (default)
```

## Dictionary Methods

```python
person = {"name": "Alice", "age": 25}

person["city"] = "NYC"     # Add/update
del person["age"]          # Delete

person.keys()              # dict_keys(['name', 'city'])
person.values()            # dict_values(['Alice', 'NYC'])
person.items()             # dict_items([('name', 'Alice'), ...])

"name" in person           # True (check key exists)
```

## Iteration

```python
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex04_dictionaries/ -v
```
