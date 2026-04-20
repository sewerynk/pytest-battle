"""
Exercise 09: Loops

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""


def sum_range(n: int) -> int:
    """Return the sum of all integers from 0 to n-1.

    Args:
        n: Upper bound (exclusive)

    Returns:
        Sum of 0 + 1 + 2 + ... + (n-1)
    """
    # TODO: Use a for loop or range() to sum integers from 0 to n-1
    pass


def count_even(numbers: list) -> int:
    """Count how many even numbers are in the list.

    Args:
        numbers: A list of integers

    Returns:
        The count of even numbers
    """
    # TODO: Loop through numbers and count even ones (n % 2 == 0)
    pass


def build_squares(n: int) -> list:
    """Return a list of squares: [1^2, 2^2, ..., n^2].

    Args:
        n: Upper bound (inclusive)

    Returns:
        A list [1, 4, 9, ..., n*n]
    """
    # TODO: Build and return the list of squares from 1 to n
    pass


def find_first_negative(numbers: list) -> int | None:
    """Return the first negative number in the list, or None if none found.

    Args:
        numbers: A list of integers

    Returns:
        The first negative integer, or None
    """
    # TODO: Loop through numbers and return the first one that is < 0
    pass


def flatten_nested(nested: list) -> list:
    """Flatten a list of lists into a single list.

    Args:
        nested: A list of lists, e.g. [[1, 2], [3, 4]]

    Returns:
        A single flat list, e.g. [1, 2, 3, 4]
    """
    # TODO: Use nested loops to flatten the list
    pass


def countdown(n: int) -> list:
    """Return a list counting down from n to 1 using a while loop.

    Args:
        n: Starting value (positive integer)

    Returns:
        A list [n, n-1, ..., 2, 1]
    """
    # TODO: Use a while loop to build a countdown list
    pass
