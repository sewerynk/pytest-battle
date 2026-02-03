# Hints for Exercise 02

## Hint 1: F-strings

Use f-strings for string formatting:

```python
name = "Alice"
message = f"Hello, {name}!"  # "Hello, Alice!"
```

## Hint 2: String Methods

Strings have built-in methods:

```python
"hello".upper()    # "HELLO"
"HELLO".lower()    # "hello"
```

## Hint 3: String Slicing

Access characters by index:

```python
text = "Python"
text[0]   # "P" (first)
text[-1]  # "n" (last)
text[::-1]  # "nohtyP" (reversed)
```

## Hint 4: Splitting and Counting

```python
words = "hello world".split()  # ["hello", "world"]
count = len(words)  # 2
```

## Hint 5: Replace

```python
"hello world".replace(" ", "-")  # "hello-world"
```

## Hint 6: Empty String Edge Case

For counting words in an empty string:

```python
"".split()  # Returns []
len([])     # Returns 0
```
