# Hints for Exercise 05

## Hint 1: Try/Except Pattern

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

## Hint 2: Parse Integer

```python
def parse_integer(s):
    try:
        return int(s)
    except ValueError:
        return None
```

## Hint 3: List Access

```python
def get_item_safely(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default
```

## Hint 4: Raising Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative")
    if age > 150:
        raise ValidationError("Age cannot exceed 150")
```

## Hint 5: Custom Exception with Attributes

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}: only {balance} available")
```

## Hint 6: Collecting Errors

```python
def read_config(config, keys):
    result = {}
    missing = []

    for key in keys:
        if key in config:
            result[key] = config[key]
        else:
            missing.append(key)

    if missing:
        raise KeyError(f"Missing keys: {missing}")

    return result
```
