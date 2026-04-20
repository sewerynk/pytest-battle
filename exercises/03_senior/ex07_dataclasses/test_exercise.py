"""Tests for Exercise 07: Dataclasses."""

import pytest
from exercise import Point, ImmutablePoint, Student, Version


class TestPoint:
    def test_creation(self):
        p = Point(1.0, 2.0)
        assert p.x == 1.0
        assert p.y == 2.0

    def test_equality(self):
        assert Point(1.0, 2.0) == Point(1.0, 2.0)
        assert Point(1.0, 2.0) != Point(3.0, 4.0)

    def test_repr(self):
        p = Point(1.0, 2.0)
        assert "1.0" in repr(p)
        assert "2.0" in repr(p)

    def test_mutable(self):
        p = Point(1.0, 2.0)
        p.x = 5.0
        assert p.x == 5.0


class TestImmutablePoint:
    def test_creation(self):
        p = ImmutablePoint(3.0, 4.0)
        assert p.x == 3.0
        assert p.y == 4.0

    def test_frozen(self):
        p = ImmutablePoint(3.0, 4.0)
        with pytest.raises(Exception):
            p.x = 10.0  # Should raise FrozenInstanceError

    def test_hashable(self):
        p1 = ImmutablePoint(1.0, 2.0)
        p2 = ImmutablePoint(3.0, 4.0)
        s = {p1, p2}
        assert len(s) == 2


class TestStudent:
    def test_creation_with_defaults(self):
        s = Student(name="Alice")
        assert s.name == "Alice"
        assert s.grades == []

    def test_class_variable(self):
        assert Student.school == "Python Academy"
        s = Student("Bob")
        assert s.school == "Python Academy"

    def test_average_grade_empty(self):
        s = Student("Alice")
        assert s.average_grade() == 0.0

    def test_average_grade(self):
        s = Student("Bob", grades=[80.0, 90.0, 100.0])
        assert s.average_grade() == 90.0

    def test_grades_not_shared(self):
        s1 = Student("Alice")
        s2 = Student("Bob")
        s1.grades.append(100.0)
        assert s2.grades == []


class TestVersion:
    def test_creation(self):
        v = Version(1, 2, 3)
        assert v.major == 1
        assert v.minor == 2
        assert v.patch == 3

    def test_ordering(self):
        assert Version(1, 0, 0) < Version(2, 0, 0)
        assert Version(1, 1, 0) > Version(1, 0, 0)
        assert Version(1, 0, 1) > Version(1, 0, 0)
        assert Version(1, 0, 0) == Version(1, 0, 0)

    def test_sorted(self):
        versions = [Version(2, 0, 0), Version(1, 0, 0), Version(1, 1, 0)]
        assert sorted(versions) == [Version(1, 0, 0), Version(1, 1, 0), Version(2, 0, 0)]
