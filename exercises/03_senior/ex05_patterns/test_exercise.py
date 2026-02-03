"""Tests for Exercise 05: Design Patterns."""

import pytest
from exercise import (
    Observable,
    BubbleSort,
    QuickSort,
    Sorter,
    Dog,
    Cat,
    Bird,
    AnimalFactory,
    TextEditor,
    AppendCommand,
    CommandInvoker,
)


class TestObserver:
    """Tests for Observer pattern."""

    def test_notify_observers(self):
        events = []

        subject = Observable()
        subject.add_observer(lambda x: events.append(f"A: {x}"))
        subject.add_observer(lambda x: events.append(f"B: {x}"))

        subject.notify("hello")

        assert "A: hello" in events
        assert "B: hello" in events

    def test_remove_observer(self):
        events = []

        def observer(x):
            events.append(x)

        subject = Observable()
        subject.add_observer(observer)
        subject.notify("first")
        subject.remove_observer(observer)
        subject.notify("second")

        assert events == ["first"]


class TestStrategy:
    """Tests for Strategy pattern."""

    def test_bubble_sort(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        strategy = BubbleSort()
        result = strategy.sort(data)

        assert result == [1, 1, 2, 3, 4, 5, 6, 9]
        assert data == [3, 1, 4, 1, 5, 9, 2, 6]  # Original unchanged

    def test_quick_sort(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        strategy = QuickSort()
        result = strategy.sort(data)

        assert result == [1, 1, 2, 3, 4, 5, 6, 9]
        assert data == [3, 1, 4, 1, 5, 9, 2, 6]  # Original unchanged

    def test_sorter_strategy_swap(self):
        data = [3, 1, 2]

        sorter = Sorter(BubbleSort())
        result1 = sorter.sort(data)

        sorter.set_strategy(QuickSort())
        result2 = sorter.sort(data)

        assert result1 == result2 == [1, 2, 3]


class TestFactory:
    """Tests for Factory pattern."""

    def test_create_dog(self):
        animal = AnimalFactory.create("dog")
        assert isinstance(animal, Dog)
        assert animal.speak() == "Woof!"

    def test_create_cat(self):
        animal = AnimalFactory.create("cat")
        assert isinstance(animal, Cat)
        assert animal.speak() == "Meow!"

    def test_create_bird(self):
        animal = AnimalFactory.create("bird")
        assert isinstance(animal, Bird)
        assert animal.speak() == "Tweet!"

    def test_unknown_type(self):
        with pytest.raises(ValueError):
            AnimalFactory.create("unicorn")


class TestCommand:
    """Tests for Command pattern."""

    def test_append_and_undo(self):
        editor = TextEditor()
        command = AppendCommand(editor, "Hello")

        command.execute()
        assert editor.text == "Hello"

        command.undo()
        assert editor.text == ""

    def test_invoker(self):
        editor = TextEditor()
        invoker = CommandInvoker()

        invoker.execute(AppendCommand(editor, "Hello"))
        invoker.execute(AppendCommand(editor, " World"))

        assert editor.text == "Hello World"

        invoker.undo()
        assert editor.text == "Hello"

        invoker.undo()
        assert editor.text == ""

    def test_undo_all(self):
        editor = TextEditor()
        invoker = CommandInvoker()

        invoker.execute(AppendCommand(editor, "A"))
        invoker.execute(AppendCommand(editor, "B"))
        invoker.execute(AppendCommand(editor, "C"))

        assert editor.text == "ABC"

        invoker.undo_all()
        assert editor.text == ""
