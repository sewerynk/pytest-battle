# Exercise 05: Error Handling

## Learning Objectives

- Use try/except blocks
- Handle specific exceptions
- Create custom exceptions
- Use finally and else clauses

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## Try/Except Basics

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0

try:
    value = int("not a number")
except ValueError as e:
    print(f"Error: {e}")
```

## Multiple Exceptions

```python
try:
    risky_operation()
except ValueError:
    handle_value_error()
except TypeError:
    handle_type_error()
except (KeyError, IndexError):
    handle_lookup_error()
```

## Finally and Else

```python
try:
    result = operation()
except SomeError:
    handle_error()
else:
    # Runs if no exception
    process_result(result)
finally:
    # Always runs
    cleanup()
```

## Custom Exceptions

```python
class ValidationError(Exception):
    """Raised when validation fails."""
    pass

def validate(value):
    if value < 0:
        raise ValidationError("Value must be non-negative")
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex05_exceptions/ -v
```
