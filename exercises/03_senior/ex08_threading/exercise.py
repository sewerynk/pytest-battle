"""
Exercise 08: Threading

Fix the functions and classes below to make the tests pass.
Look for TODO comments for guidance.
"""

import threading
import time
from collections import Counter


def run_in_thread(func, *args) -> threading.Thread:
    """Start func in a new daemon thread and return the thread.

    Args:
        func: A callable to run in the thread
        *args: Arguments to pass to func

    Returns:
        The started Thread object (daemon=True)
    """
    # TODO: Create a Thread with target=func and args=args, set daemon=True, start it, return it
    pass


class SafeCounter:
    """A thread-safe counter using a Lock.

    Requirements:
    - __init__: initialise self.value = 0 and create a threading.Lock
    - increment(): acquire the lock, increment self.value by 1, release the lock
    - get(): return self.value
    """

    def __init__(self):
        # TODO: initialise value and lock
        pass

    def increment(self):
        # TODO: acquire lock, increment, release
        pass

    def get(self) -> int:
        # TODO: return self.value
        pass


class EventSignal:
    """Demonstrate threading.Event for signalling between threads.

    Requirements:
    - __init__: create a threading.Event stored as self.event
    - signal(): set the event
    - wait_for_signal(timeout): wait up to timeout seconds; return True if signalled, False if timed out
    """

    def __init__(self):
        # TODO: create a threading.Event
        pass

    def signal(self):
        # TODO: set the event
        pass

    def wait_for_signal(self, timeout: float) -> bool:
        # TODO: wait for the event with the given timeout, return True/False
        pass


def parallel_map(func, items: list) -> list:
    """Apply func to each item in parallel using threads.

    Each item is processed in its own thread.
    Results are collected in the original order.

    Args:
        func: A callable taking one argument
        items: A list of inputs

    Returns:
        A list of results in the same order as items
    """
    # TODO: Create one thread per item, store results by index, return in order
    pass
