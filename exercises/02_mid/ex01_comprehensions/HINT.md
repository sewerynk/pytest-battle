# Hints for Exercise 01

## Hint 1: List Comprehension Syntax

```python
[expression for item in iterable]
[expression for item in iterable if condition]
```

## Hint 2: Squares

```python
[x**2 for x in range(n)]
```

## Hint 3: Filtering

```python
[x for x in numbers if x > 0]
```

## Hint 4: Dictionary from Lists

Use `zip()` to pair up keys and values:

```python
{k: v for k, v in zip(keys, values)}
```

## Hint 5: Inverting a Dictionary

```python
{v: k for k, v in d.items()}
```

## Hint 6: Dictionary with Condition

```python
{k: v for k, v in d.items() if v >= min_value}
```

## Hint 7: Set Comprehension

```python
{len(word) for word in words}
```

## Hint 8: Nested Comprehension for Flattening

```python
[item for row in matrix for item in row]
```

The order reads left-to-right like nested for loops.
