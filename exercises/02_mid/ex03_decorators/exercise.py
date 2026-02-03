"""
Exercise 03: Decorators

Fix the decorators below to make the tests pass.
Look for TODO comments for guidance.
"""

from functools import wraps
from typing import Callable, Any


def uppercase_result(func: Callable) -> Callable:
    """Decorator that converts the function's string result to uppercase.

    Args:
        func: A function that returns a string

    Returns:
        Wrapped function that returns uppercase string
    """
    # TODO: Create a wrapper that calls func and returns result.upper()
    # Don't forget @wraps(func)
    pass


def call_counter(func: Callable) -> Callable:
    """Decorator that counts how many times a function is called.

    Adds a `.call_count` attribute to the wrapped function.

    Args:
        func: Any function

    Returns:
        Wrapped function with call_count attribute
    """
    # TODO: Create a wrapper that:
    # 1. Increments wrapper.call_count each time it's called
    # 2. Calls and returns the original function result
    # Initialize wrapper.call_count = 0 before returning
    pass


def memoize(func: Callable) -> Callable:
    """Decorator that caches function results.

    Caches results based on arguments to avoid recomputation.

    Args:
        func: A function with hashable arguments

    Returns:
        Wrapped function with caching
    """
    # TODO: Create a wrapper that:
    # 1. Checks if args are in cache, return cached result if so
    # 2. Otherwise, call func, store result in cache, return it
    # Use a dictionary as cache
    pass


def validate_positive(func: Callable) -> Callable:
    """Decorator that validates all numeric arguments are positive.

    Raises:
        ValueError: If any numeric argument is <= 0

    Args:
        func: A function with numeric arguments

    Returns:
        Wrapped function with validation
    """
    # TODO: Create a wrapper that:
    # 1. Checks all args - if any number <= 0, raise ValueError
    # 2. Otherwise call and return func normally
    pass


def retry(times: int) -> Callable:
    """Decorator factory that retries a function on exception.

    Args:
        times: Number of retry attempts

    Returns:
        A decorator that will retry the function up to `times` times
    """
    # TODO: Create a decorator that:
    # 1. Tries to call the function
    # 2. If it raises an exception, retry up to `times` total attempts
    # 3. If all attempts fail, re-raise the last exception
    pass
