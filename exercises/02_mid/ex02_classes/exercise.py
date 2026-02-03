"""
Exercise 02: Classes and OOP

Fix the classes below to make the tests pass.
Look for TODO comments for guidance.
"""

import math


class Rectangle:
    """A rectangle with width and height."""

    def __init__(self, width: float, height: float):
        """Initialize rectangle with width and height."""
        # TODO: Store width and height as instance attributes
        pass

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        # TODO: Return width * height
        pass

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        # TODO: Return 2 * (width + height)
        pass

    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        # TODO: Return True if width equals height
        pass


class BankAccount:
    """A simple bank account."""

    def __init__(self, owner: str, balance: float = 0):
        """Initialize account with owner and optional starting balance."""
        # TODO: Store owner and balance as instance attributes
        pass

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        # TODO: Add amount to balance (only if amount > 0)
        pass

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account.

        Returns:
            True if withdrawal successful, False if insufficient funds
        """
        # TODO: Subtract amount from balance if sufficient funds
        # Return True if successful, False if not enough money
        pass

    @property
    def balance(self) -> float:
        """Get the current balance."""
        # TODO: Return the balance (use a private attribute _balance)
        pass


class Animal:
    """Base class for animals."""

    def __init__(self, name: str):
        """Initialize animal with a name."""
        self.name = name

    def speak(self) -> str:
        """Make a sound. Override in subclasses."""
        return "..."


class Dog(Animal):
    """A dog that barks."""

    def speak(self) -> str:
        """Return the dog's bark."""
        # TODO: Return "{name} says Woof!"
        pass


class Cat(Animal):
    """A cat that meows."""

    def speak(self) -> str:
        """Return the cat's meow."""
        # TODO: Return "{name} says Meow!"
        pass


class Counter:
    """A counter that tracks counts per key."""

    def __init__(self):
        """Initialize an empty counter."""
        # TODO: Initialize an empty dictionary to store counts
        pass

    def increment(self, key: str) -> None:
        """Increment the count for a key."""
        # TODO: Increment count for key (start at 1 if new)
        pass

    def get_count(self, key: str) -> int:
        """Get the count for a key."""
        # TODO: Return the count for key (0 if not found)
        pass

    def __repr__(self) -> str:
        """Return string representation."""
        # TODO: Return "Counter({counts})" where counts is the dict
        pass
