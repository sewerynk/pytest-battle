# Hints for Exercise 04

## Hint 1: Basic Generator

```python
def count_up_to(n):
    for i in range(1, n + 1):
        yield i
```

## Hint 2: Fibonacci

```python
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
```

## Hint 3: Infinite Cycle

```python
def cycle(items):
    while True:
        for item in items:
            yield item
```

## Hint 4: Chunking

```python
def chunk(iterable, size):
    items = list(iterable)
    for i in range(0, len(items), size):
        yield items[i:i + size]
```

## Hint 5: Flatten

```python
def flatten(nested):
    for sublist in nested:
        for item in sublist:
            yield item
```

Or using `yield from`:

```python
def flatten(nested):
    for sublist in nested:
        yield from sublist
```

## Hint 6: Filter Generator

```python
def filter_gen(predicate, iterable):
    for item in iterable:
        if predicate(item):
            yield item
```

## Hint 7: Map Generator

```python
def map_gen(func, iterable):
    for item in iterable:
        yield func(item)
```
