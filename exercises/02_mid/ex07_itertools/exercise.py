"""
Exercise 07: itertools

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""

import itertools


def chain_iterables(*iterables):
    """Chain multiple iterables into a single list.

    Args:
        *iterables: Any number of iterables

    Returns:
        A list with all elements from all iterables in order
    """
    # TODO: Use itertools.chain to combine iterables, return as list
    pass


def get_combinations(items: list, r: int) -> list:
    """Return all combinations of length r from items.

    Args:
        items: A list of items
        r: The length of each combination

    Returns:
        A list of tuples, each being a combination of r items
    """
    # TODO: Use itertools.combinations and return as list of tuples
    pass


def get_permutations(items: list, r: int) -> list:
    """Return all permutations of length r from items.

    Args:
        items: A list of items
        r: The length of each permutation

    Returns:
        A list of tuples, each being a permutation of r items
    """
    # TODO: Use itertools.permutations and return as list of tuples
    pass


def group_by_key(items: list, key_func) -> dict:
    """Group items by a key function.

    Note: items must already be sorted by key for groupby to work correctly.

    Args:
        items: A sorted list of items
        key_func: A function that returns the grouping key

    Returns:
        A dict mapping each key to a list of items with that key
    """
    # TODO: Use itertools.groupby to group items, return as dict
    pass


def take_while_positive(numbers: list) -> list:
    """Take numbers from the list while they are positive (> 0).

    Args:
        numbers: A list of integers

    Returns:
        A list of leading positive numbers (stops at first non-positive)
    """
    # TODO: Use itertools.takewhile to filter leading positives
    pass


def cycle_take(iterable, n: int) -> list:
    """Cycle through an iterable and take the first n elements.

    Args:
        iterable: Any iterable
        n: Number of elements to take

    Returns:
        A list of n elements cycling through the iterable
    """
    # TODO: Use itertools.cycle and itertools.islice to take n elements
    pass
