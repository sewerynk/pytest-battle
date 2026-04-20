"""Tests for Exercise 08: Sets."""

from exercise import (
    create_set,
    remove_duplicates,
    union_sets,
    intersection_sets,
    difference_sets,
    is_subset,
)


def test_create_set():
    result = create_set()
    assert result == {1, 2, 3}
    assert isinstance(result, set)


def test_remove_duplicates():
    result = remove_duplicates([1, 2, 2, 3, 3, 3])
    assert isinstance(result, list)
    assert sorted(result) == [1, 2, 3]

    result2 = remove_duplicates([5, 5, 5])
    assert sorted(result2) == [5]

    result3 = remove_duplicates([1, 2, 3])
    assert sorted(result3) == [1, 2, 3]


def test_union_sets():
    assert union_sets({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}
    assert union_sets({1, 2}, {3, 4}) == {1, 2, 3, 4}
    assert union_sets(set(), {1}) == {1}


def test_intersection_sets():
    assert intersection_sets({1, 2, 3}, {2, 3, 4}) == {2, 3}
    assert intersection_sets({1, 2}, {3, 4}) == set()
    assert intersection_sets({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_difference_sets():
    assert difference_sets({1, 2, 3}, {2, 3}) == {1}
    assert difference_sets({1, 2, 3}, {4, 5}) == {1, 2, 3}
    assert difference_sets({1, 2}, {1, 2, 3}) == set()


def test_is_subset():
    assert is_subset({1, 2}, {1, 2, 3}) is True
    assert is_subset({1, 2, 3}, {1, 2, 3}) is True
    assert is_subset({1, 4}, {1, 2, 3}) is False
    assert is_subset(set(), {1, 2}) is True
