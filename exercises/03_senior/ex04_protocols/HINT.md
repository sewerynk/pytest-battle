# Hints for Exercise 04

## Hint 1: Runtime Checkable Protocol

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
```

## Hint 2: Generic Stack

```python
class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)
```

## Hint 3: Find Min/Max

```python
def find_min(items: list[CT]) -> CT:
    if not items:
        raise ValueError("Empty list")
    result = items[0]
    for item in items[1:]:
        if item < result:
            result = item
    return result
```

## Hint 4: BiDict

```python
class BiDict(Generic[KT, VT]):
    def __init__(self):
        self._forward: dict[KT, VT] = {}
        self._reverse: dict[VT, KT] = {}

    def put(self, key: KT, value: VT) -> None:
        # Remove old mappings if they exist
        if key in self._forward:
            old_value = self._forward[key]
            del self._reverse[old_value]

        if value in self._reverse:
            old_key = self._reverse[value]
            del self._forward[old_key]

        self._forward[key] = value
        self._reverse[value] = key

    def get_by_key(self, key: KT) -> VT | None:
        return self._forward.get(key)

    def get_by_value(self, value: VT) -> KT | None:
        return self._reverse.get(value)

    def __len__(self) -> int:
        return len(self._forward)
```
