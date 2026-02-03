# Hints for Exercise 02

## Hint 1: Storing Instance Attributes

```python
def __init__(self, width, height):
    self.width = width
    self.height = height
```

## Hint 2: Using @property

For BankAccount, use a private attribute with a property:

```python
def __init__(self, owner, balance=0):
    self.owner = owner
    self._balance = balance  # private

@property
def balance(self):
    return self._balance
```

## Hint 3: Conditional Logic in Methods

```python
def deposit(self, amount):
    if amount > 0:
        self._balance += amount
```

## Hint 4: Return Values from Methods

```python
def withdraw(self, amount):
    if amount <= self._balance:
        self._balance -= amount
        return True
    return False
```

## Hint 5: Inheritance and super()

```python
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
```

Note: `self.name` is inherited from `Animal`.

## Hint 6: Dictionaries for Counting

```python
def __init__(self):
    self._counts = {}

def increment(self, key):
    if key in self._counts:
        self._counts[key] += 1
    else:
        self._counts[key] = 1
```

Or use `.get()`:

```python
def increment(self, key):
    self._counts[key] = self._counts.get(key, 0) + 1
```

## Hint 7: __repr__ Method

```python
def __repr__(self):
    return f"Counter({self._counts})"
```
