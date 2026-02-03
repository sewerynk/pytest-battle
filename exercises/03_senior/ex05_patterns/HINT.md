# Hints for Exercise 05

## Hint 1: Observable

```python
class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer(data)
```

## Hint 2: Bubble Sort

```python
def sort(self, data):
    result = data.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result
```

## Hint 3: Quick Sort

```python
def sort(self, data):
    if len(data) <= 1:
        return data.copy()

    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    return self.sort(left) + middle + self.sort(right)
```

## Hint 4: Sorter Context

```python
class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)
```

## Hint 5: Animal Factory

```python
@staticmethod
def create(animal_type):
    factories = {
        "dog": Dog,
        "cat": Cat,
        "bird": Bird,
    }
    if animal_type not in factories:
        raise ValueError(f"Unknown animal: {animal_type}")
    return factories[animal_type]()
```

## Hint 6: Command Pattern

```python
class AppendCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.append(self.text)

    def undo(self):
        self.editor.delete_last(len(self.text))


class CommandInvoker:
    def __init__(self):
        self._history = []

    def execute(self, command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            command = self._history.pop()
            command.undo()

    def undo_all(self):
        while self._history:
            self.undo()
```
