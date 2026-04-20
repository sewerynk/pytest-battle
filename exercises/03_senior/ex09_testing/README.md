# Exercise 09: Advanced pytest Patterns

## Learning Objectives

- Use `pytest.fixture` to share setup between tests
- Use `unittest.mock.MagicMock` to mock dependencies
- Use `@pytest.mark.parametrize` for data-driven tests
- Test exception handling in production code

## Instructions

Fix the classes in `exercise.py` to make all tests pass.

The test file demonstrates real-world testing patterns — read it carefully to understand what each class must do.

## Key Concepts

```python
import pytest
from unittest.mock import MagicMock

# Fixture: shared setup
@pytest.fixture
def my_obj():
    return MyClass()

# Mock: replace real dependencies
mock = MagicMock()
mock.some_method.return_value = 42
mock.some_method(1, 2)
mock.some_method.assert_called_once_with(1, 2)

# Parametrize: run test with multiple inputs
@pytest.mark.parametrize("x,expected", [(1, 2), (3, 6)])
def test_double(x, expected):
    assert x * 2 == expected

# Testing exceptions
with pytest.raises(ValueError):
    int("not a number")
```

## Run Tests

```bash
uv run pytest exercises/03_senior/ex09_testing/ -v
```
