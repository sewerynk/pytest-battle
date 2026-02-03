"""Tests for Exercise 03: Lists."""

from exercise import (
    create_number_list,
    get_first_element,
    get_last_element,
    sum_list,
    find_max,
    find_min,
    reverse_list,
    append_element,
    remove_duplicates,
)


def test_create_number_list():
    """Test creating number lists."""
    assert create_number_list(5) == [1, 2, 3, 4, 5]
    assert create_number_list(1) == [1]
    assert create_number_list(3) == [1, 2, 3]


def test_get_first_element():
    """Test getting first element."""
    assert get_first_element([1, 2, 3]) == 1
    assert get_first_element(["a", "b", "c"]) == "a"
    assert get_first_element([42]) == 42


def test_get_last_element():
    """Test getting last element."""
    assert get_last_element([1, 2, 3]) == 3
    assert get_last_element(["a", "b", "c"]) == "c"
    assert get_last_element([42]) == 42


def test_sum_list():
    """Test list summing."""
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([10, 20, 30]) == 60
    assert sum_list([]) == 0
    assert sum_list([-1, 1]) == 0


def test_find_max():
    """Test finding maximum."""
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([42]) == 42
    assert find_max([-5, -1, -10]) == -1


def test_find_min():
    """Test finding minimum."""
    assert find_min([1, 5, 3, 9, 2]) == 1
    assert find_min([42]) == 42
    assert find_min([-5, -1, -10]) == -10


def test_reverse_list():
    """Test list reversal."""
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list(["a", "b", "c"]) == ["c", "b", "a"]
    assert reverse_list([1]) == [1]
    assert reverse_list([]) == []


def test_reverse_list_no_mutation():
    """Test that reverse_list doesn't modify the original."""
    original = [1, 2, 3]
    reverse_list(original)
    assert original == [1, 2, 3]


def test_append_element():
    """Test appending elements."""
    assert append_element([1, 2], 3) == [1, 2, 3]
    assert append_element([], "a") == ["a"]
    assert append_element(["x"], "y") == ["x", "y"]


def test_append_element_no_mutation():
    """Test that append_element doesn't modify the original."""
    original = [1, 2]
    append_element(original, 3)
    assert original == [1, 2]


def test_remove_duplicates():
    """Test duplicate removal."""
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([]) == []
