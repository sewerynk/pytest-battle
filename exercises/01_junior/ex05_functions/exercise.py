"""
Exercise 05: Functions

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""


def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    # TODO: Return the sum of a and b
    pass


def multiply(a: int, b: int = 1) -> int:
    """Multiply two numbers with a default multiplier.

    Args:
        a: First number
        b: Second number (default is 1)

    Returns:
        The product of a and b
    """
    # TODO: Return a * b
    pass


def is_even(n: int) -> bool:
    """Check if a number is even.

    Args:
        n: The number to check

    Returns:
        True if n is even, False otherwise
    """
    # TODO: Return True if n is even, False otherwise
    pass


def is_positive(n: int) -> bool:
    """Check if a number is positive.

    Args:
        n: The number to check

    Returns:
        True if n > 0, False otherwise
    """
    # TODO: Return True if n is positive (greater than 0)
    pass


def get_min_max(numbers: list[int]) -> tuple[int, int]:
    """Get the minimum and maximum values from a list.

    Args:
        numbers: A non-empty list of integers

    Returns:
        A tuple (min_value, max_value)
    """
    # TODO: Return a tuple with (min, max) of the numbers
    pass


def add_all(*args) -> int:
    """Add all arguments together.

    Args:
        *args: Variable number of integers

    Returns:
        The sum of all arguments
    """
    # TODO: Return the sum of all arguments
    pass


def create_greeting(name: str, *, greeting: str = "Hello", punctuation: str = "!") -> str:
    """Create a customizable greeting.

    Args:
        name: The name to greet
        greeting: The greeting word (keyword-only, default "Hello")
        punctuation: The punctuation to use (keyword-only, default "!")

    Returns:
        The formatted greeting string
    """
    # TODO: Return "{greeting}, {name}{punctuation}"
    pass


def apply_operation(a: int, b: int, operation):
    """Apply an operation function to two numbers.

    Args:
        a: First number
        b: Second number
        operation: A function that takes two numbers and returns a result

    Returns:
        The result of operation(a, b)
    """
    # TODO: Call the operation function with a and b and return the result
    pass
