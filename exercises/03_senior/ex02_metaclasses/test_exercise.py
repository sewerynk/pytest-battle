"""Tests for Exercise 02: Metaclasses."""

import pytest
from exercise import (
    SingletonMeta,
    AutoReprMeta,
    ValidatedMeta,
    RegistryMeta,
    FrozenMeta,
    enforce_types,
)


class TestSingletonMeta:
    """Tests for SingletonMeta."""

    def test_same_instance(self):
        class Database(metaclass=SingletonMeta):
            def __init__(self, url):
                self.url = url

        db1 = Database("postgres://localhost")
        db2 = Database("mysql://localhost")

        assert db1 is db2
        assert db1.url == "postgres://localhost"  # First init wins


class TestAutoReprMeta:
    """Tests for AutoReprMeta."""

    def test_auto_repr(self):
        class Person(metaclass=AutoReprMeta):
            def __init__(self, name, age):
                self.name = name
                self.age = age

        p = Person("Alice", 25)
        repr_str = repr(p)

        assert "Person" in repr_str
        assert "name" in repr_str
        assert "Alice" in repr_str
        assert "age" in repr_str
        assert "25" in repr_str


class TestValidatedMeta:
    """Tests for ValidatedMeta."""

    def test_valid_class(self):
        class ValidatedBase(type):
            required_methods = ["process"]

            def __new__(mcs, name, bases, namespace):
                return ValidatedMeta.__new__(mcs, name, bases, namespace)

        class Worker(metaclass=ValidatedBase):
            def process(self):
                return "working"

        w = Worker()
        assert w.process() == "working"

    def test_invalid_class(self):
        class StrictMeta(ValidatedMeta):
            required_methods = ["save", "load"]

        with pytest.raises(TypeError, match="save|load"):
            class Invalid(metaclass=StrictMeta):
                def save(self):
                    pass
                # Missing load method!


class TestRegistryMeta:
    """Tests for RegistryMeta."""

    def test_registers_classes(self):
        # Clear registry
        RegistryMeta.registry.clear()

        class Animal(metaclass=RegistryMeta):
            pass

        class Dog(metaclass=RegistryMeta):
            pass

        assert RegistryMeta.get_class("Animal") is Animal
        assert RegistryMeta.get_class("Dog") is Dog
        assert RegistryMeta.get_class("Unknown") is None


class TestFrozenMeta:
    """Tests for FrozenMeta."""

    def test_existing_attribute(self):
        class Config(metaclass=FrozenMeta):
            debug = False

        Config.debug = True  # OK - exists
        assert Config.debug is True

    def test_new_attribute(self):
        class Config(metaclass=FrozenMeta):
            debug = False

        with pytest.raises(AttributeError):
            Config.new_attr = "value"


class TestEnforceTypes:
    """Tests for enforce_types decorator."""

    def test_valid_types(self):
        @enforce_types
        class Person:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age

        p = Person("Alice", 25)
        assert p.name == "Alice"
        assert p.age == 25

    def test_invalid_type(self):
        @enforce_types
        class Person:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age

        with pytest.raises(TypeError):
            Person("Alice", "not an int")
