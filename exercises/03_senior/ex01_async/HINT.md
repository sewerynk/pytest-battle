# Hints for Exercise 01

## Hint 1: Delay Return

```python
async def delay_return(value, delay):
    await asyncio.sleep(delay)
    return value
```

## Hint 2: Fetch All with Gather

```python
async def fetch_all(urls):
    async def fetch_one(url):
        await asyncio.sleep(0.1)
        return f"Response from {url}"

    return await asyncio.gather(*[fetch_one(url) for url in urls])
```

## Hint 3: First Completed

```python
async def first_completed(coros):
    done, pending = await asyncio.wait(
        coros,
        return_when=asyncio.FIRST_COMPLETED
    )
    # Cancel pending tasks
    for task in pending:
        task.cancel()
    # Return result of completed task
    return done.pop().result()
```

## Hint 4: With Timeout

```python
async def with_timeout(coro, timeout, default=None):
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return default
```

## Hint 5: Async Counter with Lock

```python
class AsyncCounter:
    def __init__(self):
        self._count = 0
        self._lock = asyncio.Lock()

    async def increment(self):
        async with self._lock:
            self._count += 1
            return self._count

    async def get_count(self):
        return self._count
```

## Hint 6: Async Context Manager

```python
async def __aenter__(self):
    await asyncio.sleep(0.01)
    self.is_open = True
    return self

async def __aexit__(self, exc_type, exc_val, exc_tb):
    await asyncio.sleep(0.01)
    self.is_open = False
    return False
```
