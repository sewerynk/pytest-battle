"""
Exercise 09: Advanced pytest Patterns

Fix the functions and classes below to make the tests pass.
Look for TODO comments for guidance.
"""

from unittest.mock import MagicMock, patch


class EmailSender:
    """Sends emails via an external SMTP service."""

    def send(self, to: str, subject: str, body: str) -> bool:
        """Send an email. Returns True on success."""
        raise NotImplementedError("Real SMTP not configured in tests")


class NotificationService:
    """Sends notifications using an EmailSender."""

    def __init__(self, sender: EmailSender):
        self.sender = sender
        self.sent_count = 0

    def notify(self, user_email: str, message: str) -> bool:
        """Send a notification email.

        Returns True if email was sent successfully.
        Increments self.sent_count on success.
        """
        # TODO: Call self.sender.send() with user_email, subject="Notification", body=message
        # If it returns True, increment self.sent_count and return True
        # Otherwise return False
        pass


class DataProcessor:
    """Processes data with a configurable transform function."""

    def __init__(self, transform):
        self.transform = transform

    def process_all(self, items: list) -> list:
        """Apply self.transform to each item and return the results.

        Args:
            items: A list of items to process

        Returns:
            A list of transformed items
        """
        # TODO: Apply self.transform to each item in items, return results as list
        pass

    def process_with_fallback(self, item, fallback):
        """Apply self.transform to item. If it raises any exception, return fallback.

        Args:
            item: The item to process
            fallback: Value to return if transform raises

        Returns:
            Transformed item or fallback
        """
        # TODO: Try to call self.transform(item), return fallback on any exception
        pass


class Cache:
    """A simple dict-based cache."""

    def __init__(self):
        self._store: dict = {}
        self.hits = 0
        self.misses = 0

    def get(self, key, default=None):
        """Return value for key, tracking hits/misses.

        Increments self.hits if key is found, self.misses otherwise.
        """
        # TODO: look up key; update hits/misses; return value or default
        pass

    def set(self, key, value):
        """Store value under key."""
        # TODO: store value in _store
        pass

    def clear(self):
        """Remove all entries and reset counters."""
        # TODO: clear _store and reset hits/misses to 0
        pass
