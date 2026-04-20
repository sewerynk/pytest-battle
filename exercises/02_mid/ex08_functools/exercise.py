"""
Exercise 08: functools

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""

import functools


def make_multiplier(factor: int):
    """Use functools.partial to create a multiplier function.

    Args:
        factor: The multiplication factor

    Returns:
        A function that takes a number and multiplies it by factor
    """
    # TODO: Use functools.partial with a multiply function to return a multiplier
    pass


def reduce_sum(numbers: list) -> int:
    """Sum all numbers using functools.reduce.

    Args:
        numbers: A non-empty list of integers

    Returns:
        The sum of all numbers
    """
    # TODO: Use functools.reduce to sum the list
    pass


def reduce_product(numbers: list) -> int:
    """Multiply all numbers together using functools.reduce.

    Args:
        numbers: A non-empty list of integers

    Returns:
        The product of all numbers
    """
    # TODO: Use functools.reduce to multiply all numbers together
    pass


def cached_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using functools.lru_cache for memoization.

    Args:
        n: A non-negative integer

    Returns:
        The nth Fibonacci number (fib(0)=0, fib(1)=1)
    """
    # TODO: Implement fibonacci with @functools.lru_cache decorator
    # Hint: define a helper with @functools.lru_cache inside this function or at module level
    pass


def sort_by_last_char(strings: list) -> list:
    """Sort strings by their last character using functools.cmp_to_key.

    Args:
        strings: A list of non-empty strings

    Returns:
        A list sorted by the last character of each string
    """
    # TODO: Use functools.cmp_to_key with a comparator that compares last chars
    pass
