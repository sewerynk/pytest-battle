"""
Exercise 04: Dictionaries

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""


def create_person(name: str, age: int) -> dict:
    """Create a person dictionary.

    Args:
        name: The person's name
        age: The person's age

    Returns:
        A dictionary with 'name' and 'age' keys
    """
    # TODO: Return a dictionary with "name" and "age" keys
    pass


def get_value(d: dict, key: str, default=None):
    """Get a value from a dictionary with a default.

    Args:
        d: The dictionary
        key: The key to look up
        default: The default value if key doesn't exist

    Returns:
        The value for the key, or default if not found
    """
    # TODO: Return the value for key, or default if key doesn't exist
    pass


def add_key(d: dict, key: str, value) -> dict:
    """Add a key-value pair to a dictionary.

    Args:
        d: The original dictionary
        key: The key to add
        value: The value to add

    Returns:
        A new dictionary with the key-value pair added
    """
    # TODO: Return a new dictionary with the key-value pair added
    # Don't modify the original dictionary
    pass


def remove_key(d: dict, key: str) -> dict:
    """Remove a key from a dictionary.

    Args:
        d: The original dictionary
        key: The key to remove

    Returns:
        A new dictionary without the key
    """
    # TODO: Return a new dictionary without the specified key
    # Don't modify the original dictionary
    pass


def get_keys(d: dict) -> list:
    """Get all keys from a dictionary.

    Args:
        d: The dictionary

    Returns:
        A list of all keys
    """
    # TODO: Return a list of all keys in the dictionary
    pass


def get_values(d: dict) -> list:
    """Get all values from a dictionary.

    Args:
        d: The dictionary

    Returns:
        A list of all values
    """
    # TODO: Return a list of all values in the dictionary
    pass


def count_words(text: str) -> dict:
    """Count the occurrences of each word in a text.

    Args:
        text: The input text

    Returns:
        A dictionary mapping words to their counts
    """
    # TODO: Return a dictionary with word counts
    # Example: "hello hello world" -> {"hello": 2, "world": 1}
    pass


def merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dictionaries.

    Args:
        d1: First dictionary
        d2: Second dictionary (values override d1 if keys conflict)

    Returns:
        A new merged dictionary
    """
    # TODO: Return a new dictionary combining both
    # d2 values should override d1 for duplicate keys
    pass
