"""Tests for Exercise 06: Algorithms."""

import pytest
from exercise import (
    binary_search,
    merge_sort,
    bfs,
    dfs,
    fibonacci_dp,
    longest_common_subsequence,
    knapsack,
    is_valid_parentheses,
)


class TestBinarySearch:
    """Tests for binary search."""

    def test_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13]
        assert binary_search(arr, 7) == 3
        assert binary_search(arr, 1) == 0
        assert binary_search(arr, 13) == 6

    def test_not_found(self):
        arr = [1, 3, 5, 7, 9]
        assert binary_search(arr, 4) == -1
        assert binary_search(arr, 0) == -1
        assert binary_search(arr, 10) == -1

    def test_empty(self):
        assert binary_search([], 5) == -1


class TestMergeSort:
    """Tests for merge sort."""

    def test_basic(self):
        assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_already_sorted(self):
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_empty(self):
        assert merge_sort([]) == []

    def test_single(self):
        assert merge_sort([42]) == [42]

    def test_no_mutation(self):
        original = [3, 1, 2]
        merge_sort(original)
        assert original == [3, 1, 2]


class TestBFS:
    """Tests for BFS."""

    def test_linear(self):
        graph = {"A": ["B"], "B": ["C"], "C": []}
        assert bfs(graph, "A") == ["A", "B", "C"]

    def test_tree(self):
        graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F"],
            "D": [],
            "E": [],
            "F": [],
        }
        result = bfs(graph, "A")
        assert result[0] == "A"
        assert set(result[1:3]) == {"B", "C"}

    def test_with_cycle(self):
        graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
        result = bfs(graph, "A")
        assert result == ["A", "B", "C"]


class TestDFS:
    """Tests for DFS."""

    def test_linear(self):
        graph = {"A": ["B"], "B": ["C"], "C": []}
        assert dfs(graph, "A") == ["A", "B", "C"]

    def test_with_cycle(self):
        graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
        result = dfs(graph, "A")
        assert set(result) == {"A", "B", "C"}
        assert len(result) == 3


class TestFibonacciDP:
    """Tests for Fibonacci with DP."""

    def test_base_cases(self):
        assert fibonacci_dp(0) == 0
        assert fibonacci_dp(1) == 1

    def test_sequence(self):
        assert fibonacci_dp(2) == 1
        assert fibonacci_dp(3) == 2
        assert fibonacci_dp(4) == 3
        assert fibonacci_dp(5) == 5
        assert fibonacci_dp(10) == 55

    def test_large(self):
        assert fibonacci_dp(30) == 832040


class TestLCS:
    """Tests for longest common subsequence."""

    def test_basic(self):
        assert longest_common_subsequence("ABCD", "ACD") == 3

    def test_no_common(self):
        assert longest_common_subsequence("ABC", "XYZ") == 0

    def test_same(self):
        assert longest_common_subsequence("ABC", "ABC") == 3

    def test_empty(self):
        assert longest_common_subsequence("", "ABC") == 0
        assert longest_common_subsequence("ABC", "") == 0


class TestKnapsack:
    """Tests for knapsack problem."""

    def test_basic(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        assert knapsack(weights, values, 50) == 220  # Items 1 and 2

    def test_take_all(self):
        weights = [1, 1, 1]
        values = [10, 20, 30]
        assert knapsack(weights, values, 5) == 60

    def test_none_fit(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        assert knapsack(weights, values, 5) == 0

    def test_empty(self):
        assert knapsack([], [], 10) == 0


class TestValidParentheses:
    """Tests for valid parentheses."""

    def test_valid(self):
        assert is_valid_parentheses("()") is True
        assert is_valid_parentheses("()[]{}") is True
        assert is_valid_parentheses("{[()]}") is True
        assert is_valid_parentheses("") is True

    def test_invalid(self):
        assert is_valid_parentheses("(]") is False
        assert is_valid_parentheses("([)]") is False
        assert is_valid_parentheses("{") is False
        assert is_valid_parentheses("}") is False
