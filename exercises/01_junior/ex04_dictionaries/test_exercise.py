"""Tests for Exercise 04: Dictionaries."""

from exercise import (
    create_person,
    get_value,
    add_key,
    remove_key,
    get_keys,
    get_values,
    count_words,
    merge_dicts,
)


def test_create_person():
    """Test person dictionary creation."""
    person = create_person("Alice", 25)
    assert person == {"name": "Alice", "age": 25}

    person = create_person("Bob", 30)
    assert person == {"name": "Bob", "age": 30}


def test_get_value():
    """Test getting values with defaults."""
    d = {"a": 1, "b": 2}
    assert get_value(d, "a") == 1
    assert get_value(d, "c") is None
    assert get_value(d, "c", "default") == "default"


def test_add_key():
    """Test adding keys."""
    d = {"a": 1}
    result = add_key(d, "b", 2)
    assert result == {"a": 1, "b": 2}


def test_add_key_no_mutation():
    """Test that add_key doesn't modify original."""
    d = {"a": 1}
    add_key(d, "b", 2)
    assert d == {"a": 1}


def test_remove_key():
    """Test removing keys."""
    d = {"a": 1, "b": 2}
    result = remove_key(d, "b")
    assert result == {"a": 1}


def test_remove_key_no_mutation():
    """Test that remove_key doesn't modify original."""
    d = {"a": 1, "b": 2}
    remove_key(d, "b")
    assert d == {"a": 1, "b": 2}


def test_get_keys():
    """Test getting keys."""
    d = {"a": 1, "b": 2, "c": 3}
    keys = get_keys(d)
    assert sorted(keys) == ["a", "b", "c"]


def test_get_values():
    """Test getting values."""
    d = {"a": 1, "b": 2, "c": 3}
    values = get_values(d)
    assert sorted(values) == [1, 2, 3]


def test_count_words():
    """Test word counting."""
    assert count_words("hello hello world") == {"hello": 2, "world": 1}
    assert count_words("a") == {"a": 1}
    assert count_words("") == {}


def test_merge_dicts():
    """Test dictionary merging."""
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    result = merge_dicts(d1, d2)
    assert result == {"a": 1, "b": 3, "c": 4}


def test_merge_dicts_no_mutation():
    """Test that merge doesn't modify originals."""
    d1 = {"a": 1}
    d2 = {"b": 2}
    merge_dicts(d1, d2)
    assert d1 == {"a": 1}
    assert d2 == {"b": 2}
