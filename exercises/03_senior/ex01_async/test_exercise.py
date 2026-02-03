"""Tests for Exercise 01: Async/Await."""

import asyncio
import time
import pytest
from exercise import (
    delay_return,
    fetch_all,
    first_completed,
    with_timeout,
    AsyncCounter,
    AsyncResource,
)


@pytest.mark.asyncio
async def test_delay_return():
    """Test delayed return."""
    start = time.time()
    result = await delay_return("hello", 0.1)
    elapsed = time.time() - start

    assert result == "hello"
    assert elapsed >= 0.1


@pytest.mark.asyncio
async def test_fetch_all():
    """Test concurrent fetching."""
    urls = ["http://a.com", "http://b.com", "http://c.com"]

    start = time.time()
    results = await fetch_all(urls)
    elapsed = time.time() - start

    assert len(results) == 3
    assert results[0] == "Response from http://a.com"
    assert results[1] == "Response from http://b.com"
    assert results[2] == "Response from http://c.com"

    # Should be concurrent, not sequential
    # 3 fetches at 0.1s each should take ~0.1s, not 0.3s
    assert elapsed < 0.25


@pytest.mark.asyncio
async def test_first_completed():
    """Test first completed."""

    async def slow():
        await asyncio.sleep(1)
        return "slow"

    async def fast():
        await asyncio.sleep(0.05)
        return "fast"

    result = await first_completed([slow(), fast()])
    assert result == "fast"


@pytest.mark.asyncio
async def test_with_timeout_success():
    """Test successful completion within timeout."""

    async def quick():
        await asyncio.sleep(0.05)
        return "done"

    result = await with_timeout(quick(), timeout=1.0)
    assert result == "done"


@pytest.mark.asyncio
async def test_with_timeout_exceeded():
    """Test timeout being exceeded."""

    async def slow():
        await asyncio.sleep(1.0)
        return "done"

    result = await with_timeout(slow(), timeout=0.1, default="timeout")
    assert result == "timeout"


@pytest.mark.asyncio
async def test_async_counter():
    """Test async counter with concurrent increments."""
    counter = AsyncCounter()

    async def increment_many():
        for _ in range(100):
            await counter.increment()

    # Run concurrent incrementers
    await asyncio.gather(
        increment_many(),
        increment_many(),
        increment_many(),
    )

    count = await counter.get_count()
    assert count == 300


@pytest.mark.asyncio
async def test_async_resource():
    """Test async context manager."""
    resource = AsyncResource("test")

    assert resource.is_open is False

    async with resource as r:
        assert r is resource
        assert resource.is_open is True

    assert resource.is_open is False


@pytest.mark.asyncio
async def test_async_resource_exception():
    """Test async context manager with exception."""
    resource = AsyncResource("test")

    with pytest.raises(ValueError):
        async with resource:
            raise ValueError("Error")

    assert resource.is_open is False
