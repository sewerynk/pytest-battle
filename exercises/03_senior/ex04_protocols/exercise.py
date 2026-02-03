"""
Exercise 04: Protocols & Type Hints

Fix the protocols and types below to make the tests pass.
Look for TODO comments for guidance.
"""

from typing import Protocol, TypeVar, Generic, runtime_checkable, Iterator


# TODO: Make this protocol runtime_checkable
class Comparable(Protocol):
    """Protocol for objects that can be compared."""

    def __lt__(self, other) -> bool:
        """Less than comparison."""
        ...

    def __le__(self, other) -> bool:
        """Less than or equal comparison."""
        ...


# TODO: Make this protocol runtime_checkable
class Hashable(Protocol):
    """Protocol for objects that can be hashed."""

    def __hash__(self) -> int:
        """Return hash value."""
        ...


class Serializable(Protocol):
    """Protocol for objects that can be serialized."""

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        ...

    @classmethod
    def from_dict(cls, data: dict) -> "Serializable":
        """Create from dictionary."""
        ...


T = TypeVar("T")


class Stack(Generic[T]):
    """A generic stack implementation."""

    def __init__(self):
        """Initialize empty stack."""
        # TODO: Initialize empty list
        pass

    def push(self, item: T) -> None:
        """Push item onto stack."""
        # TODO: Append item to stack
        pass

    def pop(self) -> T:
        """Pop item from stack."""
        # TODO: Remove and return top item
        # Raise IndexError if empty
        pass

    def peek(self) -> T:
        """Look at top item without removing."""
        # TODO: Return top item without removing
        # Raise IndexError if empty
        pass

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        # TODO: Return True if empty
        pass

    def __len__(self) -> int:
        """Return number of items."""
        # TODO: Return length
        pass


CT = TypeVar("CT", bound=Comparable)


def find_min(items: list[CT]) -> CT:
    """Find minimum item in a list of comparable items.

    Args:
        items: Non-empty list of comparable items

    Returns:
        The minimum item

    Raises:
        ValueError: If list is empty
    """
    # TODO: Find and return minimum item
    # Raise ValueError if empty
    pass


def find_max(items: list[CT]) -> CT:
    """Find maximum item in a list of comparable items.

    Args:
        items: Non-empty list of comparable items

    Returns:
        The maximum item

    Raises:
        ValueError: If list is empty
    """
    # TODO: Find and return maximum item
    # Raise ValueError if empty
    pass


KT = TypeVar("KT")
VT = TypeVar("VT")


class BiDict(Generic[KT, VT]):
    """A bidirectional dictionary that maps keys to values and values to keys.

    Both keys and values must be unique.
    """

    def __init__(self):
        """Initialize empty bidirectional dict."""
        # TODO: Initialize forward and reverse mappings
        pass

    def put(self, key: KT, value: VT) -> None:
        """Add a key-value pair.

        Overwrites existing mappings if key or value already exist.
        """
        # TODO: Handle existing key or value, then add mapping
        pass

    def get_by_key(self, key: KT) -> VT | None:
        """Get value by key."""
        # TODO: Return value or None
        pass

    def get_by_value(self, value: VT) -> KT | None:
        """Get key by value."""
        # TODO: Return key or None
        pass

    def __len__(self) -> int:
        """Return number of pairs."""
        # TODO: Return count
        pass
