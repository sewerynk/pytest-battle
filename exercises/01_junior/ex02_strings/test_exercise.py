"""Tests for Exercise 02: Strings."""

from exercise import (
    greet,
    shout,
    whisper,
    get_first_char,
    get_last_char,
    reverse_string,
    count_words,
    replace_spaces,
)


def test_greet():
    """Test greeting function."""
    assert greet("World") == "Hello, World!"
    assert greet("Python") == "Hello, Python!"
    assert greet("Alice") == "Hello, Alice!"


def test_shout():
    """Test uppercase conversion."""
    assert shout("hello") == "HELLO"
    assert shout("Python") == "PYTHON"
    assert shout("HeLLo WoRLd") == "HELLO WORLD"


def test_whisper():
    """Test lowercase conversion."""
    assert whisper("HELLO") == "hello"
    assert whisper("Python") == "python"
    assert whisper("HeLLo WoRLd") == "hello world"


def test_get_first_char():
    """Test getting first character."""
    assert get_first_char("Python") == "P"
    assert get_first_char("hello") == "h"
    assert get_first_char("123") == "1"


def test_get_last_char():
    """Test getting last character."""
    assert get_last_char("Python") == "n"
    assert get_last_char("hello") == "o"
    assert get_last_char("123") == "3"


def test_reverse_string():
    """Test string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("a") == "a"
    assert reverse_string("12345") == "54321"


def test_count_words():
    """Test word counting."""
    assert count_words("hello world") == 2
    assert count_words("one two three four") == 4
    assert count_words("single") == 1
    assert count_words("") == 0


def test_replace_spaces():
    """Test space replacement."""
    assert replace_spaces("hello world", "-") == "hello-world"
    assert replace_spaces("a b c", "_") == "a_b_c"
    assert replace_spaces("no spaces", "") == "nospaces"
