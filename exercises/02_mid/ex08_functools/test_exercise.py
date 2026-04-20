"""Tests for Exercise 08: functools."""

from exercise import (
    make_multiplier,
    reduce_sum,
    reduce_product,
    cached_fibonacci,
    sort_by_last_char,
)


def test_make_multiplier():
    double = make_multiplier(2)
    triple = make_multiplier(3)
    assert double(5) == 10
    assert double(0) == 0
    assert triple(4) == 12
    assert triple(7) == 21


def test_reduce_sum():
    assert reduce_sum([1, 2, 3, 4, 5]) == 15
    assert reduce_sum([10]) == 10
    assert reduce_sum([-1, 1]) == 0


def test_reduce_product():
    assert reduce_product([1, 2, 3, 4]) == 24
    assert reduce_product([5]) == 5
    assert reduce_product([2, 3, 4]) == 24


def test_cached_fibonacci():
    assert cached_fibonacci(0) == 0
    assert cached_fibonacci(1) == 1
    assert cached_fibonacci(2) == 1
    assert cached_fibonacci(5) == 5
    assert cached_fibonacci(10) == 55
    assert cached_fibonacci(20) == 6765


def test_sort_by_last_char():
    result = sort_by_last_char(["apple", "zebra", "cat", "dog"])
    # last chars: e, a, t, g → sorted: zebra(a), apple(e), dog(g), cat(t)
    assert result == ["zebra", "apple", "dog", "cat"]

    result2 = sort_by_last_char(["bc", "aa", "ab"])
    # last chars: c, a, b → sorted: aa(a), ab(b), bc(c)
    assert result2 == ["aa", "ab", "bc"]
