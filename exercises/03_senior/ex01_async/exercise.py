"""
Exercise 01: Async/Await

Fix the async functions below to make the tests pass.
Look for TODO comments for guidance.
"""

import asyncio
from typing import Any


async def delay_return(value: Any, delay: float) -> Any:
    """Return a value after a delay.

    Args:
        value: The value to return
        delay: Seconds to wait before returning

    Returns:
        The value after the delay
    """
    # TODO: Use asyncio.sleep for the delay, then return value
    pass


async def fetch_all(urls: list[str]) -> list[str]:
    """Simulate fetching multiple URLs concurrently.

    Each "fetch" should take 0.1 seconds and return
    f"Response from {url}"

    Args:
        urls: List of URLs to fetch

    Returns:
        List of responses in the same order as urls
    """
    # TODO: Create an async function to simulate fetching one URL
    # Use asyncio.gather to fetch all URLs concurrently
    pass


async def first_completed(coros: list) -> Any:
    """Return the result of the first coroutine to complete.

    Args:
        coros: List of coroutines

    Returns:
        Result of the first coroutine to complete
    """
    # TODO: Use asyncio.wait with FIRST_COMPLETED
    # Or use asyncio.as_completed
    pass


async def with_timeout(coro, timeout: float, default: Any = None) -> Any:
    """Run a coroutine with a timeout.

    Args:
        coro: The coroutine to run
        timeout: Maximum seconds to wait
        default: Value to return on timeout

    Returns:
        Coroutine result or default on timeout
    """
    # TODO: Use asyncio.wait_for with a try/except for TimeoutError
    pass


class AsyncCounter:
    """An async counter that can be incremented concurrently."""

    def __init__(self):
        """Initialize counter to 0."""
        # TODO: Initialize count and an asyncio.Lock
        pass

    async def increment(self) -> int:
        """Safely increment and return the new count."""
        # TODO: Use the lock to safely increment
        pass

    async def get_count(self) -> int:
        """Get the current count."""
        # TODO: Return the current count
        pass


class AsyncResource:
    """An async context manager for a resource."""

    def __init__(self, name: str):
        """Initialize with a name."""
        self.name = name
        self.is_open = False

    async def __aenter__(self):
        """Open the resource."""
        # TODO: Set is_open to True, simulate async open with sleep(0.01)
        # Return self
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close the resource."""
        # TODO: Set is_open to False, simulate async close with sleep(0.01)
        # Return False
        pass
