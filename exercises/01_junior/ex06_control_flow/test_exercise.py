"""Tests for Exercise 06: Control Flow."""

from exercise import (
    check_sign,
    fizzbuzz,
    count_vowels,
    sum_until,
    find_first_negative,
    get_even_numbers,
    factorial,
    is_prime,
)


def test_check_sign():
    """Test sign checking."""
    assert check_sign(5) == "positive"
    assert check_sign(-5) == "negative"
    assert check_sign(0) == "zero"


def test_fizzbuzz():
    """Test FizzBuzz."""
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == "7"
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(30) == "FizzBuzz"


def test_count_vowels():
    """Test vowel counting."""
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("Python") == 1
    assert count_vowels("") == 0


def test_sum_until():
    """Test sum until stop value."""
    assert sum_until([1, 2, 3, 4, 5], 3) == 3  # 1 + 2
    assert sum_until([1, 2, 3, 4, 5], 10) == 15  # no stop, sum all
    assert sum_until([5, 4, 3, 2, 1], 5) == 0  # stop at first
    assert sum_until([], 5) == 0


def test_find_first_negative():
    """Test finding first negative."""
    assert find_first_negative([1, -2, 3, -4]) == -2
    assert find_first_negative([1, 2, 3]) is None
    assert find_first_negative([-1, -2, -3]) == -1
    assert find_first_negative([]) is None


def test_get_even_numbers():
    """Test filtering even numbers."""
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([1, 3, 5]) == []
    assert get_even_numbers([2, 4, 6]) == [2, 4, 6]
    assert get_even_numbers([]) == []


def test_factorial():
    """Test factorial calculation."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_is_prime():
    """Test prime number check."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
