"""
Exercise 04: Generators

Fix the generators below to make the tests pass.
Look for TODO comments for guidance.
"""

from typing import Iterator, Generator


def count_up_to(n: int) -> Generator[int, None, None]:
    """Generate numbers from 1 to n (inclusive).

    Args:
        n: The upper limit

    Yields:
        Numbers 1, 2, 3, ..., n
    """
    # TODO: Use yield to generate numbers from 1 to n
    pass


def fibonacci(limit: int) -> Generator[int, None, None]:
    """Generate Fibonacci numbers up to (but not exceeding) limit.

    Args:
        limit: Maximum value to yield

    Yields:
        Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ... up to limit
    """
    # TODO: Generate Fibonacci numbers until they exceed limit
    pass


def cycle(items: list) -> Generator:
    """Infinitely cycle through items in a list.

    Args:
        items: List of items to cycle through

    Yields:
        Items from the list, repeating infinitely
    """
    # TODO: Yield items from the list, starting over when reaching the end
    # This generator is infinite!
    pass


def chunk(iterable, size: int) -> Generator[list, None, None]:
    """Split an iterable into chunks of a given size.

    Args:
        iterable: Any iterable
        size: Size of each chunk

    Yields:
        Lists of `size` elements (last chunk may be smaller)
    """
    # TODO: Yield chunks of the iterable
    pass


def flatten(nested: list) -> Generator:
    """Flatten a nested list structure (one level deep).

    Args:
        nested: A list of lists

    Yields:
        Elements from each sublist in order
    """
    # TODO: Yield elements from each sublist
    pass


def filter_gen(predicate, iterable) -> Generator:
    """Filter items using a predicate function.

    Args:
        predicate: Function that returns True/False
        iterable: Items to filter

    Yields:
        Items where predicate(item) is True
    """
    # TODO: Yield items that pass the predicate
    pass


def map_gen(func, iterable) -> Generator:
    """Apply a function to each item.

    Args:
        func: Function to apply
        iterable: Items to transform

    Yields:
        Transformed items
    """
    # TODO: Yield func(item) for each item
    pass
