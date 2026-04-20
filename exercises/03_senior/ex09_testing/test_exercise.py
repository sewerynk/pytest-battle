"""Tests for Exercise 09: Advanced pytest Patterns.

This exercise teaches:
- Using pytest fixtures
- Mocking with unittest.mock
- Parametrized tests
- Testing exceptions
"""

import pytest
from unittest.mock import MagicMock, call
from exercise import NotificationService, EmailSender, DataProcessor, Cache


# ──── Fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def mock_sender():
    """A mocked EmailSender."""
    sender = MagicMock(spec=EmailSender)
    sender.send.return_value = True
    return sender


@pytest.fixture
def notification_service(mock_sender):
    return NotificationService(sender=mock_sender)


@pytest.fixture
def cache():
    return Cache()


# ──── NotificationService tests ───────────────────────────────────────────────

class TestNotificationService:
    def test_notify_success(self, notification_service, mock_sender):
        result = notification_service.notify("user@example.com", "Hello!")
        assert result is True
        mock_sender.send.assert_called_once_with(
            "user@example.com", "Notification", "Hello!"
        )

    def test_notify_increments_count(self, notification_service):
        notification_service.notify("a@b.com", "msg")
        notification_service.notify("c@d.com", "msg2")
        assert notification_service.sent_count == 2

    def test_notify_failure(self, notification_service, mock_sender):
        mock_sender.send.return_value = False
        result = notification_service.notify("a@b.com", "msg")
        assert result is False
        assert notification_service.sent_count == 0


# ──── DataProcessor tests ────────────────────────────────────────────────────

class TestDataProcessor:
    @pytest.mark.parametrize("items,expected", [
        ([1, 2, 3], [2, 4, 6]),
        ([], []),
        ([0], [0]),
    ])
    def test_process_all(self, items, expected):
        proc = DataProcessor(lambda x: x * 2)
        assert proc.process_all(items) == expected

    def test_process_with_fallback_success(self):
        proc = DataProcessor(lambda x: x + 10)
        assert proc.process_with_fallback(5, -1) == 15

    def test_process_with_fallback_on_error(self):
        def boom(x):
            raise ValueError("oops")

        proc = DataProcessor(boom)
        assert proc.process_with_fallback(5, -1) == -1

    def test_process_with_fallback_type_error(self):
        proc = DataProcessor(lambda x: x + "bad")
        assert proc.process_with_fallback(5, None) is None


# ──── Cache tests ─────────────────────────────────────────────────────────────

class TestCache:
    def test_set_and_get(self, cache):
        cache.set("key", "value")
        assert cache.get("key") == "value"

    def test_get_missing_default(self, cache):
        assert cache.get("missing") is None
        assert cache.get("missing", "fallback") == "fallback"

    def test_hits_and_misses(self, cache):
        cache.set("a", 1)
        cache.get("a")
        cache.get("a")
        cache.get("b")
        assert cache.hits == 2
        assert cache.misses == 1

    def test_clear(self, cache):
        cache.set("x", 1)
        cache.get("x")
        cache.get("y")
        cache.clear()
        assert cache.get("x") is None
        assert cache.hits == 0
        assert cache.misses == 1  # the get("x") after clear
