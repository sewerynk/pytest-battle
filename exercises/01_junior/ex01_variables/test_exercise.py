"""Tests for Exercise 01: Variables and Data Types."""

from exercise import (
    get_integer,
    get_float,
    get_string,
    get_boolean,
    convert_string_to_int,
    convert_int_to_string,
    swap_values,
)


def test_get_integer():
    """Test that get_integer returns 42."""
    result = get_integer()
    assert result == 42
    assert isinstance(result, int)


def test_get_float():
    """Test that get_float returns 3.14."""
    result = get_float()
    assert result == 3.14
    assert isinstance(result, float)


def test_get_string():
    """Test that get_string returns 'Hello, Python!'."""
    result = get_string()
    assert result == "Hello, Python!"
    assert isinstance(result, str)


def test_get_boolean():
    """Test that get_boolean returns True."""
    result = get_boolean()
    assert result is True
    assert isinstance(result, bool)


def test_convert_string_to_int():
    """Test string to integer conversion."""
    assert convert_string_to_int("42") == 42
    assert convert_string_to_int("0") == 0
    assert convert_string_to_int("-17") == -17
    assert convert_string_to_int("100") == 100


def test_convert_int_to_string():
    """Test integer to string conversion."""
    assert convert_int_to_string(42) == "42"
    assert convert_int_to_string(0) == "0"
    assert convert_int_to_string(-17) == "-17"


def test_swap_values():
    """Test value swapping."""
    assert swap_values(1, 2) == (2, 1)
    assert swap_values("a", "b") == ("b", "a")
    assert swap_values(True, False) == (False, True)
