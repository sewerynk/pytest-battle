# Hints for Exercise 05

## Hint 1: Basic Return

```python
def add(a, b):
    return a + b
```

## Hint 2: Default Arguments

```python
def multiply(a, b=1):
    return a * b
```

## Hint 3: Checking Even/Odd

Use the modulo operator:

```python
def is_even(n):
    return n % 2 == 0
```

## Hint 4: Returning Multiple Values

```python
def get_min_max(numbers):
    return (min(numbers), max(numbers))
```

## Hint 5: Using *args

```python
def add_all(*args):
    return sum(args)
```

## Hint 6: Keyword-Only Arguments

The `*` in the function signature means everything after is keyword-only:

```python
def greet(name, *, greeting="Hello"):
    return f"{greeting}, {name}"
```

## Hint 7: Higher-Order Functions

A function can receive and call another function:

```python
def apply_operation(a, b, operation):
    return operation(a, b)
```
