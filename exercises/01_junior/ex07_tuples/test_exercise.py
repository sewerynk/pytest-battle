"""Tests for Exercise 07: Tuples."""

from exercise import (
    create_tuple,
    get_first_last,
    unpack_coordinates,
    count_occurrences,
    concatenate_tuples,
    tuple_to_list_and_back,
)


def test_create_tuple():
    result = create_tuple()
    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_get_first_last():
    assert get_first_last((10, 20, 30)) == (10, 30)
    assert get_first_last(("a", "b", "c", "d")) == ("a", "d")
    assert get_first_last((42,)) == (42, 42)


def test_unpack_coordinates():
    assert unpack_coordinates((1, 2, 3)) == (1, 2, 3)
    assert unpack_coordinates((0, -1, 5)) == (0, -1, 5)


def test_count_occurrences():
    assert count_occurrences((1, 2, 2, 3, 2), 2) == 3
    assert count_occurrences((1, 2, 3), 5) == 0
    assert count_occurrences(("a", "b", "a"), "a") == 2


def test_concatenate_tuples():
    assert concatenate_tuples((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert concatenate_tuples((), (1,)) == (1,)
    assert concatenate_tuples((1, 2), ()) == (1, 2)


def test_tuple_to_list_and_back():
    result = tuple_to_list_and_back((1, 2, 3))
    assert result == (1, 2, 3, 99)
    assert isinstance(result, tuple)

    result2 = tuple_to_list_and_back(())
    assert result2 == (99,)
