"""Tests for Exercise 04: Protocols & Type Hints."""

import pytest
from exercise import (
    Comparable,
    Hashable,
    Serializable,
    Stack,
    find_min,
    find_max,
    BiDict,
)


class TestProtocols:
    """Tests for protocols."""

    def test_comparable_runtime_check(self):
        """Test Comparable is runtime checkable."""
        assert isinstance(5, Comparable)
        assert isinstance("hello", Comparable)

    def test_hashable_runtime_check(self):
        """Test Hashable is runtime checkable."""
        assert isinstance(5, Hashable)
        assert isinstance("hello", Hashable)
        assert isinstance((1, 2), Hashable)

    def test_serializable_structural(self):
        """Test Serializable works structurally."""

        class User:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age

            def to_dict(self) -> dict:
                return {"name": self.name, "age": self.age}

            @classmethod
            def from_dict(cls, data: dict) -> "User":
                return cls(data["name"], data["age"])

        # Should work with Serializable-accepting functions
        user = User("Alice", 25)
        data = user.to_dict()
        assert data == {"name": "Alice", "age": 25}


class TestStack:
    """Tests for generic Stack."""

    def test_push_pop(self):
        stack: Stack[int] = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_peek(self):
        stack: Stack[str] = Stack()
        stack.push("a")
        stack.push("b")

        assert stack.peek() == "b"
        assert stack.peek() == "b"  # Still there

    def test_is_empty(self):
        stack: Stack[int] = Stack()
        assert stack.is_empty() is True

        stack.push(1)
        assert stack.is_empty() is False

    def test_len(self):
        stack: Stack[int] = Stack()
        assert len(stack) == 0

        stack.push(1)
        stack.push(2)
        assert len(stack) == 2

    def test_pop_empty(self):
        stack: Stack[int] = Stack()
        with pytest.raises(IndexError):
            stack.pop()

    def test_peek_empty(self):
        stack: Stack[int] = Stack()
        with pytest.raises(IndexError):
            stack.peek()


class TestFindMinMax:
    """Tests for find_min and find_max."""

    def test_find_min(self):
        assert find_min([3, 1, 4, 1, 5]) == 1
        assert find_min([5]) == 5
        assert find_min(["c", "a", "b"]) == "a"

    def test_find_max(self):
        assert find_max([3, 1, 4, 1, 5]) == 5
        assert find_max([5]) == 5
        assert find_max(["c", "a", "b"]) == "c"

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            find_min([])
        with pytest.raises(ValueError):
            find_max([])


class TestBiDict:
    """Tests for BiDict."""

    def test_basic_operations(self):
        bd: BiDict[str, int] = BiDict()
        bd.put("a", 1)
        bd.put("b", 2)

        assert bd.get_by_key("a") == 1
        assert bd.get_by_value(1) == "a"
        assert bd.get_by_key("b") == 2
        assert bd.get_by_value(2) == "b"

    def test_not_found(self):
        bd: BiDict[str, int] = BiDict()
        assert bd.get_by_key("missing") is None
        assert bd.get_by_value(999) is None

    def test_overwrite_key(self):
        bd: BiDict[str, int] = BiDict()
        bd.put("a", 1)
        bd.put("a", 2)  # Overwrite

        assert bd.get_by_key("a") == 2
        assert bd.get_by_value(1) is None  # Old value gone
        assert bd.get_by_value(2) == "a"

    def test_overwrite_value(self):
        bd: BiDict[str, int] = BiDict()
        bd.put("a", 1)
        bd.put("b", 1)  # Same value, different key

        assert bd.get_by_key("a") is None  # Old key gone
        assert bd.get_by_key("b") == 1
        assert bd.get_by_value(1) == "b"

    def test_len(self):
        bd: BiDict[str, int] = BiDict()
        assert len(bd) == 0

        bd.put("a", 1)
        bd.put("b", 2)
        assert len(bd) == 2
