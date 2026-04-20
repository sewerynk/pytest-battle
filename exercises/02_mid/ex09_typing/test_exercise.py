"""Tests for Exercise 09: Type Hints and Annotations."""

from exercise import (
    typed_identity,
    first_or_default,
    apply,
    filter_by_type,
    zip_to_dict,
    flatten_optional,
)


def test_typed_identity():
    assert typed_identity(42) == 42
    assert typed_identity("hello") == "hello"
    assert typed_identity([1, 2, 3]) == [1, 2, 3]
    assert typed_identity(None) is None


def test_first_or_default():
    assert first_or_default([1, 2, 3], 0) == 1
    assert first_or_default([], 0) == 0
    assert first_or_default([], "default") == "default"
    assert first_or_default(["a", "b"], "x") == "a"


def test_apply():
    assert apply(lambda x: x * 2, 5) == 10
    assert apply(str.upper, "hello") == "HELLO"
    assert apply(lambda x: x + 1, 0) == 1


def test_filter_by_type():
    mixed = [1, "hello", 2.5, 3, "world", True]
    assert filter_by_type(mixed, int) == [1, 3, True]
    assert filter_by_type(mixed, str) == ["hello", "world"]
    assert filter_by_type(mixed, float) == [2.5]
    assert filter_by_type([], int) == []


def test_zip_to_dict():
    assert zip_to_dict(["a", "b", "c"], [1, 2, 3]) == {"a": 1, "b": 2, "c": 3}
    assert zip_to_dict([], []) == {}
    assert zip_to_dict(["x"], [42]) == {"x": 42}


def test_flatten_optional():
    assert flatten_optional([1, None, 2, None, 3]) == [1, 2, 3]
    assert flatten_optional([None, None]) == []
    assert flatten_optional([1, 2, 3]) == [1, 2, 3]
    assert flatten_optional([]) == []
