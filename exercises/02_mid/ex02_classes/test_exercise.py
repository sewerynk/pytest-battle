"""Tests for Exercise 02: Classes and OOP."""

from exercise import Rectangle, BankAccount, Animal, Dog, Cat, Counter


class TestRectangle:
    """Tests for Rectangle class."""

    def test_init(self):
        rect = Rectangle(10, 5)
        assert rect.width == 10
        assert rect.height == 5

    def test_area(self):
        rect = Rectangle(10, 5)
        assert rect.area() == 50

    def test_perimeter(self):
        rect = Rectangle(10, 5)
        assert rect.perimeter() == 30

    def test_is_square_false(self):
        rect = Rectangle(10, 5)
        assert rect.is_square() is False

    def test_is_square_true(self):
        square = Rectangle(5, 5)
        assert square.is_square() is True


class TestBankAccount:
    """Tests for BankAccount class."""

    def test_init_default_balance(self):
        account = BankAccount("Alice")
        assert account.owner == "Alice"
        assert account.balance == 0

    def test_init_with_balance(self):
        account = BankAccount("Bob", 100)
        assert account.balance == 100

    def test_deposit(self):
        account = BankAccount("Alice", 100)
        account.deposit(50)
        assert account.balance == 150

    def test_deposit_negative_ignored(self):
        account = BankAccount("Alice", 100)
        account.deposit(-50)
        assert account.balance == 100

    def test_withdraw_success(self):
        account = BankAccount("Alice", 100)
        result = account.withdraw(30)
        assert result is True
        assert account.balance == 70

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("Alice", 100)
        result = account.withdraw(150)
        assert result is False
        assert account.balance == 100


class TestInheritance:
    """Tests for Animal inheritance."""

    def test_animal_base(self):
        animal = Animal("Generic")
        assert animal.name == "Generic"
        assert animal.speak() == "..."

    def test_dog(self):
        dog = Dog("Buddy")
        assert dog.name == "Buddy"
        assert dog.speak() == "Buddy says Woof!"

    def test_cat(self):
        cat = Cat("Whiskers")
        assert cat.name == "Whiskers"
        assert cat.speak() == "Whiskers says Meow!"


class TestCounter:
    """Tests for Counter class."""

    def test_init(self):
        counter = Counter()
        assert counter.get_count("a") == 0

    def test_increment(self):
        counter = Counter()
        counter.increment("a")
        assert counter.get_count("a") == 1
        counter.increment("a")
        assert counter.get_count("a") == 2

    def test_multiple_keys(self):
        counter = Counter()
        counter.increment("a")
        counter.increment("b")
        counter.increment("a")
        assert counter.get_count("a") == 2
        assert counter.get_count("b") == 1

    def test_repr(self):
        counter = Counter()
        counter.increment("a")
        assert repr(counter) == "Counter({'a': 1})"
