"""
Exercise 05: Error Handling

Fix the functions below to make the tests pass.
Look for TODO comments for guidance.
"""


class ValidationError(Exception):
    """Custom exception for validation errors."""
    # TODO: This is already complete - just inherit from Exception
    pass


class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""

    def __init__(self, balance: float, amount: float):
        """Initialize with balance and attempted amount."""
        # TODO: Store balance and amount as attributes
        # Call super().__init__ with a message like:
        # "Cannot withdraw {amount}: only {balance} available"
        pass


def safe_divide(a: float, b: float) -> float | None:
    """Safely divide two numbers.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        a / b if b != 0, else None
    """
    # TODO: Use try/except to catch ZeroDivisionError
    # Return None if division by zero
    pass


def parse_integer(s: str) -> int | None:
    """Parse a string to integer, returning None on failure.

    Args:
        s: String to parse

    Returns:
        Integer value or None if parsing fails
    """
    # TODO: Use try/except to catch ValueError
    pass


def get_item_safely(lst: list, index: int, default=None):
    """Safely get an item from a list.

    Args:
        lst: The list
        index: Index to access
        default: Value to return if index is invalid

    Returns:
        lst[index] or default if index is out of bounds
    """
    # TODO: Use try/except to catch IndexError
    pass


def validate_age(age: int) -> None:
    """Validate that age is reasonable.

    Args:
        age: The age to validate

    Raises:
        ValidationError: If age < 0 or age > 150
    """
    # TODO: Raise ValidationError with appropriate message
    # "Age cannot be negative" or "Age cannot exceed 150"
    pass


def process_payment(balance: float, amount: float) -> float:
    """Process a payment from a balance.

    Args:
        balance: Current balance
        amount: Amount to withdraw

    Returns:
        New balance after withdrawal

    Raises:
        InsufficientFundsError: If balance < amount
    """
    # TODO: Raise InsufficientFundsError if insufficient funds
    # Otherwise return balance - amount
    pass


def read_config(config: dict, keys: list[str]) -> dict:
    """Read values from config, collecting any errors.

    Args:
        config: Configuration dictionary
        keys: Keys to read from config

    Returns:
        Dictionary mapping keys to their values

    Raises:
        KeyError: If any key is missing (with message listing missing keys)
    """
    # TODO: Try to get each key from config
    # If any keys are missing, raise KeyError with list of missing keys
    # Return dict of found values
    pass
