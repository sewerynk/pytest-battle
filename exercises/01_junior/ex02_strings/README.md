# Exercise 02: Strings

## Learning Objectives

- Understand string manipulation methods
- Learn string formatting (f-strings)
- Work with string slicing

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## String Methods

```python
text = "hello world"

text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.capitalize()   # "Hello world"
text.title()        # "Hello World"
text.strip()        # Removes whitespace
text.split()        # ["hello", "world"]
text.replace("o", "0")  # "hell0 w0rld"
```

## String Formatting (f-strings)

```python
name = "Alice"
age = 25
greeting = f"Hello, {name}! You are {age} years old."
```

## String Slicing

```python
text = "Python"
text[0]      # "P"
text[-1]     # "n"
text[0:3]    # "Pyt"
text[::-1]   # "nohtyP" (reversed)
```

## Run Tests

```bash
uv run pytest exercises/01_junior/ex02_strings/ -v
```
