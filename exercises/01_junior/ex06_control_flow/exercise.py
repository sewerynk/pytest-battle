"""
Exercise 06: Control Flow

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""


def check_sign(n: int) -> str:
    """Check if a number is positive, negative, or zero.

    Args:
        n: The number to check

    Returns:
        "positive" if n > 0
        "negative" if n < 0
        "zero" if n == 0
    """
    # TODO: Return "positive", "negative", or "zero" based on n
    pass


def fizzbuzz(n: int) -> str:
    """Classic FizzBuzz problem.

    Args:
        n: A positive integer

    Returns:
        "FizzBuzz" if n is divisible by both 3 and 5
        "Fizz" if n is divisible by 3 only
        "Buzz" if n is divisible by 5 only
        str(n) otherwise
    """
    # TODO: Implement FizzBuzz logic
    pass


def count_vowels(text: str) -> int:
    """Count the number of vowels in a string.

    Args:
        text: The input string

    Returns:
        The count of vowels (a, e, i, o, u - case insensitive)
    """
    # TODO: Count and return the number of vowels
    pass


def sum_until(numbers: list[int], stop_value: int) -> int:
    """Sum numbers until a stop value is encountered.

    Args:
        numbers: A list of integers
        stop_value: Stop summing when this value is found

    Returns:
        Sum of numbers before stop_value (or all if not found)
    """
    # TODO: Sum numbers, but stop (don't include) if stop_value is found
    pass


def find_first_negative(numbers: list[int]) -> int | None:
    """Find the first negative number in a list.

    Args:
        numbers: A list of integers

    Returns:
        The first negative number, or None if no negatives found
    """
    # TODO: Return the first negative number or None
    pass


def get_even_numbers(numbers: list[int]) -> list[int]:
    """Get all even numbers from a list.

    Args:
        numbers: A list of integers

    Returns:
        A new list containing only the even numbers
    """
    # TODO: Return a list of even numbers
    pass


def factorial(n: int) -> int:
    """Calculate the factorial of n.

    Args:
        n: A non-negative integer

    Returns:
        n! (n factorial)
        0! = 1, 1! = 1, 5! = 120
    """
    # TODO: Calculate n! using a loop
    pass


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n: An integer

    Returns:
        True if n is prime, False otherwise
        Note: Numbers less than 2 are not prime
    """
    # TODO: Return True if n is prime, False otherwise
    pass
