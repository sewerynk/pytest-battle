"""Tests for Exercise 04: Generators."""

from exercise import (
    count_up_to,
    fibonacci,
    cycle,
    chunk,
    flatten,
    filter_gen,
    map_gen,
)


def test_count_up_to():
    """Test counting generator."""
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
    assert list(count_up_to(1)) == [1]
    assert list(count_up_to(0)) == []


def test_fibonacci():
    """Test Fibonacci generator."""
    assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8]
    assert list(fibonacci(1)) == [0, 1, 1]
    assert list(fibonacci(0)) == [0]


def test_cycle():
    """Test cycle generator."""
    gen = cycle([1, 2, 3])
    result = [next(gen) for _ in range(7)]
    assert result == [1, 2, 3, 1, 2, 3, 1]


def test_chunk():
    """Test chunking generator."""
    assert list(chunk([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(chunk([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(chunk([1, 2, 3], 5)) == [[1, 2, 3]]
    assert list(chunk([], 3)) == []


def test_flatten():
    """Test flatten generator."""
    assert list(flatten([[1, 2], [3, 4], [5]])) == [1, 2, 3, 4, 5]
    assert list(flatten([[1], [2], [3]])) == [1, 2, 3]
    assert list(flatten([])) == []
    assert list(flatten([[], [1], []])) == [1]


def test_filter_gen():
    """Test filter generator."""
    result = list(filter_gen(lambda x: x > 0, [-1, 0, 1, 2, -3]))
    assert result == [1, 2]

    result = list(filter_gen(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
    assert result == [2, 4, 6]


def test_map_gen():
    """Test map generator."""
    result = list(map_gen(lambda x: x * 2, [1, 2, 3]))
    assert result == [2, 4, 6]

    result = list(map_gen(str.upper, ["a", "b", "c"]))
    assert result == ["A", "B", "C"]
