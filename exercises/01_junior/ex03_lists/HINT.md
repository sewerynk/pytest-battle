# Hints for Exercise 03

## Hint 1: Creating Lists with Range

```python
list(range(1, 6))  # [1, 2, 3, 4, 5]
```

## Hint 2: Indexing

```python
lst = [1, 2, 3]
lst[0]   # First element (1)
lst[-1]  # Last element (3)
```

## Hint 3: Built-in Functions

```python
sum([1, 2, 3])  # 6
max([1, 5, 3])  # 5
min([1, 5, 3])  # 1
```

## Hint 4: Reversing Without Mutation

```python
original = [1, 2, 3]

# Using slicing (creates new list)
reversed_list = original[::-1]

# Or using list() with reversed()
reversed_list = list(reversed(original))
```

## Hint 5: Appending Without Mutation

```python
original = [1, 2]

# Create a new list
new_list = original + [3]  # [1, 2, 3]

# Or using unpacking
new_list = [*original, 3]
```

## Hint 6: Remove Duplicates While Preserving Order

```python
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen
```
