"""Tests for Exercise 08: Threading."""

import threading
import time
import pytest
from exercise import run_in_thread, SafeCounter, EventSignal, parallel_map


def test_run_in_thread():
    results = []
    def worker():
        results.append(1)

    t = run_in_thread(worker)
    assert isinstance(t, threading.Thread)
    assert t.daemon is True
    t.join(timeout=2)
    assert results == [1]


def test_run_in_thread_with_args():
    results = []
    def worker(x, y):
        results.append(x + y)

    t = run_in_thread(worker, 3, 4)
    t.join(timeout=2)
    assert results == [7]


class TestSafeCounter:
    def test_initial_value(self):
        c = SafeCounter()
        assert c.get() == 0

    def test_increment(self):
        c = SafeCounter()
        c.increment()
        assert c.get() == 1
        c.increment()
        assert c.get() == 2

    def test_thread_safe(self):
        """Many threads incrementing concurrently should produce correct total."""
        counter = SafeCounter()
        threads = [threading.Thread(target=counter.increment) for _ in range(100)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        assert counter.get() == 100


class TestEventSignal:
    def test_wait_times_out(self):
        e = EventSignal()
        result = e.wait_for_signal(timeout=0.05)
        assert result is False

    def test_signal_received(self):
        e = EventSignal()

        def sender():
            time.sleep(0.05)
            e.signal()

        t = threading.Thread(target=sender)
        t.start()
        result = e.wait_for_signal(timeout=2.0)
        t.join()
        assert result is True


def test_parallel_map():
    result = parallel_map(lambda x: x * 2, [1, 2, 3, 4, 5])
    assert result == [2, 4, 6, 8, 10]

    result2 = parallel_map(str, [1, 2, 3])
    assert result2 == ["1", "2", "3"]

    result3 = parallel_map(lambda x: x, [])
    assert result3 == []
