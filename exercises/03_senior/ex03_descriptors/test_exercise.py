"""Tests for Exercise 03: Descriptors."""

import pytest
from exercise import (
    Lazy,
    TypedAttribute,
    BoundedNumber,
    Observable,
    CachedProperty,
)


class TestLazy:
    """Tests for Lazy descriptor."""

    def test_computes_once(self):
        call_count = 0

        class MyClass:
            @Lazy
            def expensive(self):
                nonlocal call_count
                call_count += 1
                return "computed"

        obj = MyClass()
        assert obj.expensive == "computed"
        assert call_count == 1

        # Second access should use cache
        assert obj.expensive == "computed"
        assert call_count == 1

    def test_class_access(self):
        class MyClass:
            @Lazy
            def value(self):
                return 42

        assert isinstance(MyClass.value, Lazy)


class TestTypedAttribute:
    """Tests for TypedAttribute descriptor."""

    def test_valid_type(self):
        class Person:
            name = TypedAttribute(str, "")
            age = TypedAttribute(int, 0)

        p = Person()
        p.name = "Alice"
        p.age = 25

        assert p.name == "Alice"
        assert p.age == 25

    def test_invalid_type(self):
        class Person:
            age = TypedAttribute(int, 0)

        p = Person()
        with pytest.raises(TypeError):
            p.age = "not an int"

    def test_default_value(self):
        class Person:
            name = TypedAttribute(str, "Unknown")

        p = Person()
        assert p.name == "Unknown"


class TestBoundedNumber:
    """Tests for BoundedNumber descriptor."""

    def test_within_bounds(self):
        class Temperature:
            celsius = BoundedNumber(min_value=-273.15, max_value=1000)

        t = Temperature()
        t.celsius = 25.0
        assert t.celsius == 25.0

    def test_below_min(self):
        class Temperature:
            celsius = BoundedNumber(min_value=-273.15)

        t = Temperature()
        with pytest.raises(ValueError):
            t.celsius = -300

    def test_above_max(self):
        class Percentage:
            value = BoundedNumber(min_value=0, max_value=100)

        p = Percentage()
        with pytest.raises(ValueError):
            p.value = 150


class TestObservable:
    """Tests for Observable descriptor."""

    def test_observers_called(self):
        changes = []

        class Config:
            value = Observable()

        cfg = Config()
        Config.value.add_observer(
            lambda obj, old, new: changes.append((old, new))
        )

        cfg.value = 10
        cfg.value = 20

        assert changes == [(None, 10), (10, 20)]


class TestCachedProperty:
    """Tests for CachedProperty descriptor."""

    def test_caches_result(self):
        call_count = 0

        class Circle:
            def __init__(self, radius):
                self.radius = radius

            @CachedProperty
            def area(self):
                nonlocal call_count
                call_count += 1
                return 3.14159 * self.radius ** 2

        c = Circle(5)
        assert c.area == pytest.approx(78.54, rel=0.01)
        assert call_count == 1

        # Should be cached
        assert c.area == pytest.approx(78.54, rel=0.01)
        assert call_count == 1

    def test_class_access(self):
        class Circle:
            @CachedProperty
            def area(self):
                return 0

        assert isinstance(Circle.area, CachedProperty)
