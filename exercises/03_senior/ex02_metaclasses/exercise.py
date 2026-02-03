"""
Exercise 02: Metaclasses

Fix the metaclasses below to make the tests pass.
Look for TODO comments for guidance.
"""


class SingletonMeta(type):
    """Metaclass that makes classes singletons.

    Only one instance of each class using this metaclass can exist.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Return existing instance or create new one."""
        # TODO: Check if cls is in _instances
        # If not, create instance using super().__call__
        # Store and return the instance
        pass


class AutoReprMeta(type):
    """Metaclass that auto-generates __repr__ for classes."""

    def __new__(mcs, name, bases, namespace):
        """Add __repr__ method to the class."""
        # TODO: Create a __repr__ method that shows class name
        # and all instance attributes
        # Example: "Person(name='Alice', age=25)"
        pass


class ValidatedMeta(type):
    """Metaclass that validates class has required methods."""

    required_methods = []

    def __new__(mcs, name, bases, namespace):
        """Validate class has required methods."""
        # TODO: Check that all methods in required_methods exist
        # in namespace or bases
        # Raise TypeError if missing
        pass


class RegistryMeta(type):
    """Metaclass that registers all subclasses."""

    registry = {}

    def __new__(mcs, name, bases, namespace):
        """Register the class."""
        # TODO: Create the class, then add it to registry
        # registry[name] = cls
        pass

    @classmethod
    def get_class(mcs, name: str):
        """Get a registered class by name."""
        return mcs.registry.get(name)


class FrozenMeta(type):
    """Metaclass that prevents adding new class attributes after creation."""

    def __setattr__(cls, name, value):
        """Prevent setting new attributes."""
        # TODO: Only allow setting if attribute already exists
        # Raise AttributeError for new attributes
        # Hint: Use hasattr to check
        pass


def enforce_types(cls):
    """Class decorator that enforces type hints on __init__.

    Wraps __init__ to validate argument types match annotations.

    Args:
        cls: The class to decorate

    Returns:
        The decorated class with type checking
    """
    # TODO: Wrap cls.__init__ to check types
    # Get annotations from original __init__
    # Raise TypeError if any argument doesn't match its annotation
    pass
