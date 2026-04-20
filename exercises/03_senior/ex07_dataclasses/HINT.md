# Hints for Exercise 07: Dataclasses

## Point
```python
@dataclass
class Point:
    x: float
    y: float
```

## ImmutablePoint
```python
@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float
```

## Student
```python
@dataclass
class Student:
    name: str
    grades: list = field(default_factory=list)
    school: ClassVar[str] = "Python Academy"

    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
```

## Version
```python
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int
```
Note: with `order=True`, comparison is done field by field in definition order.
