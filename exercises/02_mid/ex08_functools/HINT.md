# Hints for Exercise 08: functools

## make_multiplier
```python
def multiply(x, y):
    return x * y
return functools.partial(multiply, factor)
```

## reduce_sum
```python
return functools.reduce(lambda a, b: a + b, numbers)
```

## reduce_product
```python
return functools.reduce(lambda a, b: a * b, numbers)
```

## cached_fibonacci
Define a helper at module level with the decorator:
```python
@functools.lru_cache(maxsize=None)
def _fib(n):
    if n < 2:
        return n
    return _fib(n - 1) + _fib(n - 2)

def cached_fibonacci(n):
    return _fib(n)
```

## sort_by_last_char
```python
def cmp(a, b):
    return (a[-1] > b[-1]) - (a[-1] < b[-1])
return sorted(strings, key=functools.cmp_to_key(cmp))
```
