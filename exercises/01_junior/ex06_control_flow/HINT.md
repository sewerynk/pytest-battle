# Hints for Exercise 06

## Hint 1: If/Elif/Else

```python
if n > 0:
    return "positive"
elif n < 0:
    return "negative"
else:
    return "zero"
```

## Hint 2: FizzBuzz Order

Check divisibility by both 3 AND 5 first:

```python
if n % 3 == 0 and n % 5 == 0:
    return "FizzBuzz"
elif n % 3 == 0:
    return "Fizz"
# ...
```

## Hint 3: Counting Vowels

```python
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
return count
```

## Hint 4: Using Break

```python
total = 0
for num in numbers:
    if num == stop_value:
        break  # Exit the loop
    total += num
return total
```

## Hint 5: Finding First Match

```python
for num in numbers:
    if num < 0:
        return num
return None
```

## Hint 6: Filtering with a Loop

```python
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num)
return result
```

## Hint 7: Factorial

```python
result = 1
for i in range(1, n + 1):
    result *= i
return result
```

## Hint 8: Prime Check

A number is prime if it's > 1 and has no divisors other than 1 and itself:

```python
if n < 2:
    return False
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        return False
return True
```
