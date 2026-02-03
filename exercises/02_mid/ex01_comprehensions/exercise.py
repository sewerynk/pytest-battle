"""
Exercise 01: Comprehensions

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""


def squares(n: int) -> list[int]:
    """Generate a list of squares from 0 to n-1.

    Args:
        n: The upper limit (exclusive)

    Returns:
        [0, 1, 4, 9, ...] up to (n-1)^2
    """
    # TODO: Use a list comprehension to generate squares
    pass


def filter_positive(numbers: list[int]) -> list[int]:
    """Filter only positive numbers from a list.

    Args:
        numbers: A list of integers

    Returns:
        A list containing only positive numbers
    """
    # TODO: Use a list comprehension with a condition
    pass


def word_lengths(words: list[str]) -> list[int]:
    """Get the length of each word.

    Args:
        words: A list of strings

    Returns:
        A list of word lengths
    """
    # TODO: Use a list comprehension to get lengths
    pass


def create_dict_from_lists(keys: list, values: list) -> dict:
    """Create a dictionary from two parallel lists.

    Args:
        keys: List of keys
        values: List of values

    Returns:
        A dictionary mapping keys to values
    """
    # TODO: Use a dictionary comprehension with zip
    pass


def invert_dict(d: dict) -> dict:
    """Invert a dictionary (swap keys and values).

    Args:
        d: A dictionary with unique values

    Returns:
        A dictionary with keys and values swapped
    """
    # TODO: Use a dictionary comprehension to invert
    pass


def filter_dict_by_value(d: dict, min_value: int) -> dict:
    """Filter dictionary to keep only entries with value >= min_value.

    Args:
        d: A dictionary with integer values
        min_value: The minimum value threshold

    Returns:
        A filtered dictionary
    """
    # TODO: Use a dictionary comprehension with a condition
    pass


def unique_word_lengths(words: list[str]) -> set[int]:
    """Get the unique word lengths as a set.

    Args:
        words: A list of strings

    Returns:
        A set of unique word lengths
    """
    # TODO: Use a set comprehension
    pass


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    """Flatten a 2D matrix into a 1D list.

    Args:
        matrix: A 2D list (list of lists)

    Returns:
        A flattened 1D list
    """
    # TODO: Use a nested list comprehension
    # Hint: [item for row in matrix for item in row]
    pass
