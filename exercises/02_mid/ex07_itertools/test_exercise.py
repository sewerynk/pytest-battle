"""Tests for Exercise 07: itertools."""

from exercise import (
    chain_iterables,
    get_combinations,
    get_permutations,
    group_by_key,
    take_while_positive,
    cycle_take,
)


def test_chain_iterables():
    assert chain_iterables([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert chain_iterables([1], [2], [3]) == [1, 2, 3]
    assert chain_iterables([], [1, 2]) == [1, 2]


def test_get_combinations():
    result = get_combinations([1, 2, 3], 2)
    assert sorted(result) == sorted([(1, 2), (1, 3), (2, 3)])

    result2 = get_combinations(["a", "b"], 2)
    assert result2 == [("a", "b")]


def test_get_permutations():
    result = get_permutations([1, 2, 3], 2)
    assert len(result) == 6
    assert (1, 2) in result
    assert (2, 1) in result

    result2 = get_permutations(["a", "b"], 2)
    assert sorted(result2) == [("a", "b"), ("b", "a")]


def test_group_by_key():
    data = [1, 1, 2, 2, 3]
    result = group_by_key(data, lambda x: x)
    assert result == {1: [1, 1], 2: [2, 2], 3: [3]}

    words = ["apple", "ant", "bat", "bear", "cat"]
    result2 = group_by_key(words, lambda w: w[0])
    assert result2 == {"a": ["apple", "ant"], "b": ["bat", "bear"], "c": ["cat"]}


def test_take_while_positive():
    assert take_while_positive([1, 2, 3, -1, 4]) == [1, 2, 3]
    assert take_while_positive([-1, 2, 3]) == []
    assert take_while_positive([1, 2, 3]) == [1, 2, 3]
    assert take_while_positive([]) == []


def test_cycle_take():
    assert cycle_take([1, 2], 5) == [1, 2, 1, 2, 1]
    assert cycle_take(["a", "b", "c"], 7) == ["a", "b", "c", "a", "b", "c", "a"]
    assert cycle_take([1], 3) == [1, 1, 1]
