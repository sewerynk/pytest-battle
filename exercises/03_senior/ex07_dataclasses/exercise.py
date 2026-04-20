"""
Exercise 07: Dataclasses

Fix the classes and functions below to make the tests pass.
Look for TODO comments for guidance.
"""

from dataclasses import dataclass, field
from typing import ClassVar


# TODO: Add @dataclass decorator and implement the class
class Point:
    """A 2D point with x and y coordinates.

    Requirements:
    - Fields: x (float), y (float)
    - Should support equality comparison automatically
    - Should have a readable repr automatically
    """
    # TODO: Add x: float and y: float fields
    pass


# TODO: Add @dataclass decorator with frozen=True (immutable)
class ImmutablePoint:
    """An immutable 2D point.

    Requirements:
    - Fields: x (float), y (float)
    - Should be hashable (usable in sets/dicts)
    - Should raise an error if you try to modify x or y
    """
    # TODO: Add x: float and y: float fields
    pass


# TODO: Add @dataclass decorator
class Student:
    """A student record.

    Requirements:
    - Fields: name (str), grades (list of float, default empty list)
    - Class variable: school (str) = "Python Academy"
    - Method: average_grade() -> float (returns mean of grades, or 0.0 if empty)
    """
    # TODO: Add fields and method
    pass


# TODO: Add @dataclass decorator with order=True
class Version:
    """A semantic version number.

    Requirements:
    - Fields: major (int), minor (int), patch (int)
    - order=True to enable comparison operators (<, >, <=, >=)
    """
    # TODO: Add major, minor, patch fields
    pass
