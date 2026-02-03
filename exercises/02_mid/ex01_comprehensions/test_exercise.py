"""Tests for Exercise 01: Comprehensions."""

from exercise import (
    squares,
    filter_positive,
    word_lengths,
    create_dict_from_lists,
    invert_dict,
    filter_dict_by_value,
    unique_word_lengths,
    flatten_matrix,
)


def test_squares():
    """Test squares generation."""
    assert squares(5) == [0, 1, 4, 9, 16]
    assert squares(1) == [0]
    assert squares(0) == []


def test_filter_positive():
    """Test filtering positive numbers."""
    assert filter_positive([-1, 0, 1, 2, -3]) == [1, 2]
    assert filter_positive([1, 2, 3]) == [1, 2, 3]
    assert filter_positive([-1, -2]) == []


def test_word_lengths():
    """Test word length calculation."""
    assert word_lengths(["hello", "world"]) == [5, 5]
    assert word_lengths(["a", "ab", "abc"]) == [1, 2, 3]
    assert word_lengths([]) == []


def test_create_dict_from_lists():
    """Test dictionary creation from lists."""
    assert create_dict_from_lists(["a", "b"], [1, 2]) == {"a": 1, "b": 2}
    assert create_dict_from_lists([], []) == {}


def test_invert_dict():
    """Test dictionary inversion."""
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({}) == {}


def test_filter_dict_by_value():
    """Test filtering dictionary by value."""
    d = {"a": 1, "b": 5, "c": 3, "d": 10}
    assert filter_dict_by_value(d, 5) == {"b": 5, "d": 10}
    assert filter_dict_by_value(d, 100) == {}


def test_unique_word_lengths():
    """Test unique word lengths."""
    result = unique_word_lengths(["hello", "world", "hi", "bye"])
    assert result == {2, 3, 5}


def test_flatten_matrix():
    """Test matrix flattening."""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert flatten_matrix(matrix) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten_matrix([[1], [2], [3]]) == [1, 2, 3]
    assert flatten_matrix([]) == []
