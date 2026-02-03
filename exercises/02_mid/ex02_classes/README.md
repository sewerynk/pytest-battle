# Exercise 02: Classes and OOP

## Learning Objectives

- Create classes with `__init__`
- Define instance methods and properties
- Understand inheritance
- Use `@property` decorators

## Instructions

Fix the classes in `exercise.py` to make all tests pass.

## Class Basics

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Buddy", 3)
dog.bark()  # "Buddy says woof!"
```

## Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

## Inheritance

```python
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex02_classes/ -v
```
