# Exercise 04: Protocols & Type Hints

## Learning Objectives

- Understand structural subtyping with Protocol
- Use runtime_checkable protocols
- Create generic types
- Work with TypeVar and ParamSpec

## Instructions

Fix the protocols and types in `exercise.py` to make all tests pass.

## Protocol Basics

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

def render(item: Drawable) -> str:
    return item.draw()

# Any class with a draw() method works!
class Circle:
    def draw(self) -> str:
        return "○"

render(Circle())  # Works!
```

## Runtime Checkable

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...

isinstance(file_obj, Closable)  # True if has close()
```

## Generic Types

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()
```

## Run Tests

```bash
uv run pytest exercises/03_senior/ex04_protocols/ -v
```
