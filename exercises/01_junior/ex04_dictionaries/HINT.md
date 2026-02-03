# Hints for Exercise 04

## Hint 1: Creating Dictionaries

```python
person = {"name": "Alice", "age": 25}
```

## Hint 2: Safe Access with get()

```python
d = {"a": 1}
d.get("a")              # 1
d.get("b")              # None
d.get("b", "default")   # "default"
```

## Hint 3: Creating New Dictionaries (No Mutation)

```python
original = {"a": 1}

# Using copy and update
new = original.copy()
new["b"] = 2

# Using unpacking (Python 3.5+)
new = {**original, "b": 2}
```

## Hint 4: Removing Keys Without Mutation

```python
original = {"a": 1, "b": 2}

# Using dict comprehension
new = {k: v for k, v in original.items() if k != "b"}
```

## Hint 5: Getting Keys and Values as Lists

```python
d = {"a": 1, "b": 2}
keys = list(d.keys())    # ["a", "b"]
values = list(d.values())  # [1, 2]
```

## Hint 6: Counting Words

```python
def count_words(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
```

## Hint 7: Merging Dictionaries

```python
# Using unpacking
merged = {**d1, **d2}

# Or using | operator (Python 3.9+)
merged = d1 | d2
```
