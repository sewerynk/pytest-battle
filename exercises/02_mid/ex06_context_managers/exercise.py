"""
Exercise 06: Context Managers

Fix the context managers below to make the tests pass.
Look for TODO comments for guidance.
"""

from contextlib import contextmanager
from typing import Generator


class Timer:
    """Context manager that tracks elapsed time."""

    def __init__(self):
        """Initialize the timer."""
        self.start_time = None
        self.end_time = None
        self.elapsed = None

    def __enter__(self):
        """Start the timer."""
        # TODO: Record start time using time.time()
        # Return self
        import time
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop the timer and calculate elapsed time."""
        # TODO: Record end time and calculate elapsed
        # elapsed = end_time - start_time
        # Return False (don't suppress exceptions)
        import time
        pass


class SuppressErrors:
    """Context manager that suppresses specified exception types."""

    def __init__(self, *exception_types):
        """Initialize with exception types to suppress."""
        # TODO: Store the exception types
        pass

    def __enter__(self):
        """Enter the context."""
        # TODO: Just return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit, suppressing specified exceptions."""
        # TODO: Return True if exc_type is in our exception_types
        # Return False otherwise
        pass


class Counter:
    """Context manager that counts how many times it's entered."""

    count = 0  # Class variable shared across all instances

    def __enter__(self):
        """Increment counter on enter."""
        # TODO: Increment Counter.count and return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context."""
        # TODO: Just return False
        pass


@contextmanager
def temporary_value(obj: dict, key: str, value) -> Generator:
    """Temporarily set a key in a dictionary.

    Restores the original value (or removes key) after the context.

    Args:
        obj: The dictionary to modify
        key: The key to set
        value: The temporary value

    Yields:
        The modified dictionary
    """
    # TODO: Save old value (if exists), set new value
    # yield obj
    # Restore old value or delete key in finally block
    pass


@contextmanager
def capture_output() -> Generator[list, None, None]:
    """Capture all items appended to a list during the context.

    Yields:
        A list that will contain captured items
    """
    # TODO: Create a list, yield it
    # The list automatically captures what's appended to it
    pass


@contextmanager
def transaction(data: dict) -> Generator[dict, None, None]:
    """Simple transaction-like context manager.

    If an exception occurs, rolls back changes to the dictionary.

    Args:
        data: Dictionary to operate on

    Yields:
        The dictionary (allows modifications)
    """
    # TODO: Save a copy of data before yield
    # If exception occurs, restore the original data
    # Use data.clear() and data.update(backup) to restore
    pass
