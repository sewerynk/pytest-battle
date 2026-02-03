"""Tests for Exercise 06: Context Managers."""

import time
import pytest
from exercise import (
    Timer,
    SuppressErrors,
    Counter,
    temporary_value,
    capture_output,
    transaction,
)


class TestTimer:
    """Tests for Timer context manager."""

    def test_measures_time(self):
        with Timer() as t:
            time.sleep(0.1)

        assert t.elapsed is not None
        assert t.elapsed >= 0.1
        assert t.elapsed < 0.2

    def test_attributes(self):
        with Timer() as t:
            pass

        assert t.start_time is not None
        assert t.end_time is not None
        assert t.end_time >= t.start_time


class TestSuppressErrors:
    """Tests for SuppressErrors context manager."""

    def test_suppresses_specified_error(self):
        with SuppressErrors(ValueError):
            raise ValueError("This should be suppressed")
        # Should not raise

    def test_allows_other_errors(self):
        with pytest.raises(TypeError):
            with SuppressErrors(ValueError):
                raise TypeError("This should NOT be suppressed")

    def test_multiple_exception_types(self):
        with SuppressErrors(ValueError, TypeError):
            raise ValueError("Suppressed")

        with SuppressErrors(ValueError, TypeError):
            raise TypeError("Also suppressed")


class TestCounter:
    """Tests for Counter context manager."""

    def test_counts_entries(self):
        Counter.count = 0  # Reset

        with Counter():
            assert Counter.count == 1

        with Counter():
            assert Counter.count == 2

        assert Counter.count == 2

    def test_nested(self):
        Counter.count = 0  # Reset

        with Counter():
            with Counter():
                assert Counter.count == 2


class TestTemporaryValue:
    """Tests for temporary_value context manager."""

    def test_sets_temporary_value(self):
        d = {"a": 1}
        with temporary_value(d, "a", 100) as obj:
            assert d["a"] == 100
            assert obj is d

        assert d["a"] == 1  # Restored

    def test_new_key(self):
        d = {"a": 1}
        with temporary_value(d, "b", 2):
            assert d["b"] == 2

        assert "b" not in d  # Removed

    def test_restores_on_exception(self):
        d = {"a": 1}
        with pytest.raises(ValueError):
            with temporary_value(d, "a", 100):
                raise ValueError("Error")

        assert d["a"] == 1  # Restored despite exception


class TestCaptureOutput:
    """Tests for capture_output context manager."""

    def test_captures_appends(self):
        with capture_output() as output:
            output.append("hello")
            output.append("world")

        assert output == ["hello", "world"]

    def test_empty_capture(self):
        with capture_output() as output:
            pass

        assert output == []


class TestTransaction:
    """Tests for transaction context manager."""

    def test_keeps_changes_on_success(self):
        data = {"a": 1}
        with transaction(data) as d:
            d["b"] = 2
            d["a"] = 10

        assert data == {"a": 10, "b": 2}

    def test_rollback_on_exception(self):
        data = {"a": 1, "b": 2}
        with pytest.raises(ValueError):
            with transaction(data) as d:
                d["a"] = 100
                d["c"] = 3
                raise ValueError("Rollback!")

        assert data == {"a": 1, "b": 2}  # Original state
