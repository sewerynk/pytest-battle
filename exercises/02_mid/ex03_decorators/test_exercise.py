"""Tests for Exercise 03: Decorators."""

import pytest
from exercise import (
    uppercase_result,
    call_counter,
    memoize,
    validate_positive,
    retry,
)


class TestUppercaseResult:
    """Tests for uppercase_result decorator."""

    def test_basic(self):
        @uppercase_result
        def greet(name):
            return f"hello, {name}"

        assert greet("world") == "HELLO, WORLD"

    def test_preserves_name(self):
        @uppercase_result
        def my_func():
            """My docstring."""
            return "test"

        assert my_func.__name__ == "my_func"
        assert my_func.__doc__ == "My docstring."


class TestCallCounter:
    """Tests for call_counter decorator."""

    def test_counts_calls(self):
        @call_counter
        def greet(name):
            return f"Hello, {name}"

        assert greet.call_count == 0
        greet("Alice")
        assert greet.call_count == 1
        greet("Bob")
        greet("Charlie")
        assert greet.call_count == 3

    def test_returns_correct_value(self):
        @call_counter
        def add(a, b):
            return a + b

        assert add(2, 3) == 5


class TestMemoize:
    """Tests for memoize decorator."""

    def test_caches_results(self):
        call_count = 0

        @memoize
        def expensive_func(x):
            nonlocal call_count
            call_count += 1
            return x * 2

        assert expensive_func(5) == 10
        assert call_count == 1

        # Second call with same arg should use cache
        assert expensive_func(5) == 10
        assert call_count == 1  # Still 1!

        # Different arg should compute
        assert expensive_func(10) == 20
        assert call_count == 2

    def test_multiple_args(self):
        @memoize
        def add(a, b):
            return a + b

        assert add(2, 3) == 5
        assert add(2, 3) == 5  # Cached
        assert add(3, 2) == 5  # Different args


class TestValidatePositive:
    """Tests for validate_positive decorator."""

    def test_valid_args(self):
        @validate_positive
        def multiply(a, b):
            return a * b

        assert multiply(2, 3) == 6

    def test_invalid_zero(self):
        @validate_positive
        def multiply(a, b):
            return a * b

        with pytest.raises(ValueError):
            multiply(0, 5)

    def test_invalid_negative(self):
        @validate_positive
        def multiply(a, b):
            return a * b

        with pytest.raises(ValueError):
            multiply(-1, 5)


class TestRetry:
    """Tests for retry decorator factory."""

    def test_success_first_try(self):
        @retry(times=3)
        def always_works():
            return "success"

        assert always_works() == "success"

    def test_success_after_retry(self):
        attempts = 0

        @retry(times=3)
        def fails_twice():
            nonlocal attempts
            attempts += 1
            if attempts < 3:
                raise ValueError("Not yet!")
            return "success"

        assert fails_twice() == "success"
        assert attempts == 3

    def test_all_retries_fail(self):
        @retry(times=3)
        def always_fails():
            raise ValueError("Always fails")

        with pytest.raises(ValueError, match="Always fails"):
            always_fails()
