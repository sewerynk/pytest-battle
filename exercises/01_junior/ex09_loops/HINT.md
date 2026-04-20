# Hints for Exercise 09: Loops

## sum_range
```python
total = 0
for i in range(n):
    total += i
return total
```

## count_even
```python
count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1
return count
```

## build_squares
```python
result = []
for i in range(1, n + 1):
    result.append(i * i)
return result
```

## find_first_negative
Loop and `return` as soon as you find a negative number. Return `None` after the loop.

## flatten_nested
```python
result = []
for sublist in nested:
    for item in sublist:
        result.append(item)
return result
```

## countdown
```python
result = []
while n >= 1:
    result.append(n)
    n -= 1
return result
```
