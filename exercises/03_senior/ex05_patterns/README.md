# Exercise 05: Design Patterns

## Learning Objectives

- Implement common design patterns in Python
- Understand when to use each pattern
- Apply Pythonic approaches to patterns

## Instructions

Fix the pattern implementations in `exercise.py` to make all tests pass.

## Patterns Covered

### Observer Pattern
Objects subscribe to events from a subject.

### Strategy Pattern
Swap algorithms at runtime.

### Factory Pattern
Create objects without specifying exact class.

### Decorator Pattern (not the Python decorator)
Add behavior to objects dynamically.

### Command Pattern
Encapsulate actions as objects.

## Python-Specific Notes

- Many patterns are simpler in Python due to first-class functions
- Duck typing reduces need for interface hierarchies
- Context managers and decorators cover many use cases

## Run Tests

```bash
uv run pytest exercises/03_senior/ex05_patterns/ -v
```
