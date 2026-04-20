"""Tests for Exercise 09: Loops."""

from exercise import (
    sum_range,
    count_even,
    build_squares,
    find_first_negative,
    flatten_nested,
    countdown,
)


def test_sum_range():
    assert sum_range(5) == 10   # 0+1+2+3+4
    assert sum_range(1) == 0
    assert sum_range(0) == 0
    assert sum_range(10) == 45


def test_count_even():
    assert count_even([1, 2, 3, 4, 5, 6]) == 3
    assert count_even([1, 3, 5]) == 0
    assert count_even([2, 4, 6]) == 3
    assert count_even([]) == 0


def test_build_squares():
    assert build_squares(5) == [1, 4, 9, 16, 25]
    assert build_squares(1) == [1]
    assert build_squares(3) == [1, 4, 9]


def test_find_first_negative():
    assert find_first_negative([1, -2, 3, -4]) == -2
    assert find_first_negative([1, 2, 3]) is None
    assert find_first_negative([-5, -3, 1]) == -5
    assert find_first_negative([]) is None


def test_flatten_nested():
    assert flatten_nested([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_nested([[1], [2], [3]]) == [1, 2, 3]
    assert flatten_nested([[], [1, 2]]) == [1, 2]
    assert flatten_nested([]) == []


def test_countdown():
    assert countdown(5) == [5, 4, 3, 2, 1]
    assert countdown(1) == [1]
    assert countdown(3) == [3, 2, 1]
