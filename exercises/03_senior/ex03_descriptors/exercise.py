"""
Exercise 03: Descriptors

Fix the descriptors below to make the tests pass.
Look for TODO comments for guidance.
"""

from typing import Any, Callable


class Lazy:
    """Descriptor that lazily computes a value once and caches it.

    The value is computed by calling the function once, then cached.
    """

    def __init__(self, func: Callable):
        """Initialize with the function to compute the value."""
        # TODO: Store the function
        self.func = func
        self.name = None

    def __set_name__(self, owner, name):
        """Store the attribute name."""
        # TODO: Store the name
        pass

    def __get__(self, obj, objtype=None):
        """Compute value on first access, then return cached value."""
        # TODO: If obj is None, return self (class access)
        # Otherwise, compute value if not cached, cache it, return it
        pass


class TypedAttribute:
    """Descriptor that enforces a specific type."""

    def __init__(self, expected_type: type, default: Any = None):
        """Initialize with expected type and optional default."""
        # TODO: Store expected_type and default
        pass

    def __set_name__(self, owner, name):
        """Store the attribute name."""
        # TODO: Store the name
        pass

    def __get__(self, obj, objtype=None):
        """Get the attribute value."""
        # TODO: If obj is None, return self
        # Otherwise return value from obj.__dict__ or default
        pass

    def __set__(self, obj, value):
        """Set the attribute value with type checking."""
        # TODO: Check isinstance(value, expected_type)
        # Raise TypeError if wrong type
        # Store in obj.__dict__[self.name]
        pass


class BoundedNumber:
    """Descriptor that enforces min/max bounds on a number."""

    def __init__(self, min_value: float = None, max_value: float = None):
        """Initialize with optional min and max bounds."""
        # TODO: Store min and max values
        pass

    def __set_name__(self, owner, name):
        """Store the attribute name."""
        # TODO: Store the name
        pass

    def __get__(self, obj, objtype=None):
        """Get the value."""
        # TODO: Standard descriptor get
        pass

    def __set__(self, obj, value):
        """Set the value with bounds checking."""
        # TODO: Check min_value <= value <= max_value if bounds are set
        # Raise ValueError if out of bounds
        pass


class Observable:
    """Descriptor that notifies observers when value changes."""

    def __init__(self):
        """Initialize the descriptor."""
        # TODO: Initialize storage for name and callbacks
        pass

    def __set_name__(self, owner, name):
        """Store the attribute name."""
        # TODO: Store the name
        pass

    def __get__(self, obj, objtype=None):
        """Get the value."""
        # TODO: Standard descriptor get
        pass

    def __set__(self, obj, value):
        """Set the value and notify observers."""
        # TODO: Get old value, set new value
        # Call all registered callbacks with (obj, old_value, new_value)
        pass

    def add_observer(self, callback: Callable) -> None:
        """Add an observer callback."""
        # TODO: Add callback to list
        pass


class CachedProperty:
    """Descriptor similar to @property but caches the result.

    Like functools.cached_property.
    """

    def __init__(self, func: Callable):
        """Initialize with the function to compute the value."""
        # TODO: Store the function and docstring
        pass

    def __set_name__(self, owner, name):
        """Store the attribute name."""
        # TODO: Store the name
        pass

    def __get__(self, obj, objtype=None):
        """Compute and cache the value."""
        # TODO: If obj is None, return self
        # Check if value in obj.__dict__
        # If not, compute and store
        # Return value
        pass
