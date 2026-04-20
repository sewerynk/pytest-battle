"""
Exercise 09: Type Hints and Annotations

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""

from typing import TypeVar, Callable, Any

T = TypeVar("T")


def typed_identity(value: T) -> T:
    """Return the value unchanged.

    Args:
        value: Any value

    Returns:
        The same value, preserving its type
    """
    # TODO: Return value unchanged
    pass


def first_or_default(items: list[T], default: T) -> T:
    """Return the first item of a list, or default if the list is empty.

    Args:
        items: A list of items
        default: The value to return if items is empty

    Returns:
        First element of items, or default
    """
    # TODO: Return the first item or default
    pass


def apply(func: Callable[[T], T], value: T) -> T:
    """Apply a function to a value and return the result.

    Args:
        func: A callable taking one argument
        value: The argument to pass

    Returns:
        The result of func(value)
    """
    # TODO: Call func with value and return the result
    pass


def filter_by_type(items: list[Any], target_type: type) -> list:
    """Return only items of the specified type.

    Args:
        items: A mixed list
        target_type: The type to filter for

    Returns:
        A list containing only items that are instances of target_type
    """
    # TODO: Filter items to keep only those that are instances of target_type
    pass


def zip_to_dict(keys: list, values: list) -> dict:
    """Combine two lists into a dict.

    Args:
        keys: A list of keys
        values: A list of values (same length as keys)

    Returns:
        A dict mapping keys[i] -> values[i]
    """
    # TODO: Use zip() to combine keys and values into a dict
    pass


def flatten_optional(items: list[int | None]) -> list[int]:
    """Remove None values from a list.

    Args:
        items: A list that may contain int values and None

    Returns:
        A list with None values removed
    """
    # TODO: Filter out None values from items
    pass
