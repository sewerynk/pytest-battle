"""
Exercise 05: Design Patterns

Fix the pattern implementations below to make the tests pass.
Look for TODO comments for guidance.
"""

from abc import ABC, abstractmethod
from typing import Callable, Any


# ============================================================================
# Observer Pattern
# ============================================================================

class Observable:
    """Subject that can be observed."""

    def __init__(self):
        """Initialize with empty observer list."""
        # TODO: Initialize list of observers
        pass

    def add_observer(self, observer: Callable[[Any], None]) -> None:
        """Add an observer callback."""
        # TODO: Add observer to list
        pass

    def remove_observer(self, observer: Callable[[Any], None]) -> None:
        """Remove an observer callback."""
        # TODO: Remove observer from list
        pass

    def notify(self, data: Any) -> None:
        """Notify all observers with data."""
        # TODO: Call each observer with data
        pass


# ============================================================================
# Strategy Pattern
# ============================================================================

class SortStrategy(ABC):
    """Abstract base for sorting strategies."""

    @abstractmethod
    def sort(self, data: list) -> list:
        """Sort the data and return sorted list."""
        pass


class BubbleSort(SortStrategy):
    """Bubble sort implementation."""

    def sort(self, data: list) -> list:
        """Sort using bubble sort algorithm."""
        # TODO: Implement bubble sort
        # Return a NEW sorted list (don't modify original)
        pass


class QuickSort(SortStrategy):
    """Quick sort implementation."""

    def sort(self, data: list) -> list:
        """Sort using quick sort algorithm."""
        # TODO: Implement quick sort
        # Return a NEW sorted list (don't modify original)
        pass


class Sorter:
    """Context class that uses a sorting strategy."""

    def __init__(self, strategy: SortStrategy):
        """Initialize with a sorting strategy."""
        # TODO: Store the strategy
        pass

    def set_strategy(self, strategy: SortStrategy) -> None:
        """Change the sorting strategy."""
        # TODO: Update the strategy
        pass

    def sort(self, data: list) -> list:
        """Sort data using current strategy."""
        # TODO: Delegate to strategy
        pass


# ============================================================================
# Factory Pattern
# ============================================================================

class Animal(ABC):
    """Abstract base for animals."""

    @abstractmethod
    def speak(self) -> str:
        """Make animal sound."""
        pass


class Dog(Animal):
    """A dog."""

    def speak(self) -> str:
        # TODO: Return "Woof!"
        pass


class Cat(Animal):
    """A cat."""

    def speak(self) -> str:
        # TODO: Return "Meow!"
        pass


class Bird(Animal):
    """A bird."""

    def speak(self) -> str:
        # TODO: Return "Tweet!"
        pass


class AnimalFactory:
    """Factory for creating animals."""

    @staticmethod
    def create(animal_type: str) -> Animal:
        """Create an animal by type name.

        Args:
            animal_type: "dog", "cat", or "bird"

        Returns:
            The appropriate Animal instance

        Raises:
            ValueError: If animal_type is unknown
        """
        # TODO: Return appropriate animal based on type
        # Raise ValueError for unknown types
        pass


# ============================================================================
# Command Pattern
# ============================================================================

class Command(ABC):
    """Abstract command."""

    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""
        pass

    @abstractmethod
    def undo(self) -> None:
        """Undo the command."""
        pass


class TextEditor:
    """Simple text editor that supports commands."""

    def __init__(self):
        """Initialize with empty text."""
        self.text = ""

    def append(self, text: str) -> None:
        """Append text."""
        self.text += text

    def delete_last(self, count: int) -> str:
        """Delete last N characters, return deleted text."""
        deleted = self.text[-count:]
        self.text = self.text[:-count]
        return deleted


class AppendCommand(Command):
    """Command to append text."""

    def __init__(self, editor: TextEditor, text: str):
        """Initialize with editor and text to append."""
        # TODO: Store editor and text
        pass

    def execute(self) -> None:
        """Append the text."""
        # TODO: Append text to editor
        pass

    def undo(self) -> None:
        """Remove the appended text."""
        # TODO: Delete the appended text
        pass


class CommandInvoker:
    """Invoker that executes and tracks commands."""

    def __init__(self):
        """Initialize with empty command history."""
        # TODO: Initialize history list
        pass

    def execute(self, command: Command) -> None:
        """Execute a command and add to history."""
        # TODO: Execute and store in history
        pass

    def undo(self) -> None:
        """Undo the last command."""
        # TODO: Pop last command and undo it
        pass

    def undo_all(self) -> None:
        """Undo all commands."""
        # TODO: Undo all commands in reverse order
        pass
