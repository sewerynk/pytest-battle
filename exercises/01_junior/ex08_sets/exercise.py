"""
Exercise 08: Sets

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""


def create_set() -> set:
    """Return a set containing 1, 2, 3."""
    # TODO: Return a set {1, 2, 3}
    pass


def remove_duplicates(lst: list) -> list:
    """Remove duplicate values from a list, preserving no specific order.

    Args:
        lst: A list possibly containing duplicates

    Returns:
        A list with unique elements only (order not guaranteed)
    """
    # TODO: Convert to set to remove duplicates, then back to list
    pass


def union_sets(a: set, b: set) -> set:
    """Return the union of two sets.

    Args:
        a: First set
        b: Second set

    Returns:
        A set containing all elements from both sets
    """
    # TODO: Return the union of a and b
    pass


def intersection_sets(a: set, b: set) -> set:
    """Return the intersection of two sets.

    Args:
        a: First set
        b: Second set

    Returns:
        A set containing only elements present in both sets
    """
    # TODO: Return the intersection of a and b
    pass


def difference_sets(a: set, b: set) -> set:
    """Return elements in a that are not in b.

    Args:
        a: First set
        b: Second set

    Returns:
        A set of elements in a but not in b
    """
    # TODO: Return the difference a - b
    pass


def is_subset(a: set, b: set) -> bool:
    """Check if a is a subset of b.

    Args:
        a: Potential subset
        b: Potential superset

    Returns:
        True if all elements of a are in b, False otherwise
    """
    # TODO: Return True if a is a subset of b
    pass
