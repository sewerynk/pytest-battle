# Exercise 01: Async/Await

## Learning Objectives

- Understand async/await syntax
- Create async functions and coroutines
- Use asyncio for concurrent execution
- Handle async context managers

## Instructions

Fix the async functions in `exercise.py` to make all tests pass.

## Async Basics

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Simulate I/O
    return "data"

# Running async code
result = asyncio.run(fetch_data())
```

## Concurrent Execution

```python
async def main():
    # Run concurrently
    results = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data(),
    )
    return results
```

## Async Comprehensions

```python
async def get_values():
    return [await process(x) async for x in async_iterator()]
```

## Async Context Managers

```python
class AsyncConnection:
    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.disconnect()
```

## Run Tests

```bash
uv run pytest exercises/03_senior/ex01_async/ -v
```
