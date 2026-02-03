"""Tests for Exercise 05: Functions."""

from exercise import (
    add,
    multiply,
    is_even,
    is_positive,
    get_min_max,
    add_all,
    create_greeting,
    apply_operation,
)


def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(100, 200) == 300


def test_multiply():
    """Test multiplication with default."""
    assert multiply(5, 3) == 15
    assert multiply(5) == 5  # default b=1
    assert multiply(0, 10) == 0
    assert multiply(-2, 3) == -6


def test_is_even():
    """Test even number check."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True


def test_is_positive():
    """Test positive number check."""
    assert is_positive(5) is True
    assert is_positive(0) is False
    assert is_positive(-5) is False


def test_get_min_max():
    """Test min/max tuple return."""
    assert get_min_max([1, 5, 3]) == (1, 5)
    assert get_min_max([42]) == (42, 42)
    assert get_min_max([-10, 0, 10]) == (-10, 10)


def test_add_all():
    """Test variable arguments."""
    assert add_all(1, 2, 3) == 6
    assert add_all(10) == 10
    assert add_all() == 0
    assert add_all(1, 2, 3, 4, 5) == 15


def test_create_greeting():
    """Test keyword-only arguments."""
    assert create_greeting("Alice") == "Hello, Alice!"
    assert create_greeting("Bob", greeting="Hi") == "Hi, Bob!"
    assert create_greeting("Charlie", punctuation="?") == "Hello, Charlie?"
    assert create_greeting("Diana", greeting="Hey", punctuation=".") == "Hey, Diana."


def test_apply_operation():
    """Test higher-order function."""
    assert apply_operation(10, 5, lambda a, b: a + b) == 15
    assert apply_operation(10, 5, lambda a, b: a - b) == 5
    assert apply_operation(10, 5, lambda a, b: a * b) == 50
    assert apply_operation(10, 5, lambda a, b: a // b) == 2
