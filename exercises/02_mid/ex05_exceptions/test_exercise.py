"""Tests for Exercise 05: Error Handling."""

import pytest
from exercise import (
    ValidationError,
    InsufficientFundsError,
    safe_divide,
    parse_integer,
    get_item_safely,
    validate_age,
    process_payment,
    read_config,
)


class TestSafeDivide:
    """Tests for safe_divide function."""

    def test_normal_division(self):
        assert safe_divide(10, 2) == 5.0
        assert safe_divide(7, 2) == 3.5

    def test_division_by_zero(self):
        assert safe_divide(10, 0) is None
        assert safe_divide(0, 0) is None


class TestParseInteger:
    """Tests for parse_integer function."""

    def test_valid_integer(self):
        assert parse_integer("42") == 42
        assert parse_integer("-17") == -17
        assert parse_integer("0") == 0

    def test_invalid_integer(self):
        assert parse_integer("not a number") is None
        assert parse_integer("3.14") is None
        assert parse_integer("") is None


class TestGetItemSafely:
    """Tests for get_item_safely function."""

    def test_valid_index(self):
        lst = [1, 2, 3, 4, 5]
        assert get_item_safely(lst, 0) == 1
        assert get_item_safely(lst, 2) == 3
        assert get_item_safely(lst, -1) == 5

    def test_invalid_index(self):
        lst = [1, 2, 3]
        assert get_item_safely(lst, 10) is None
        assert get_item_safely(lst, 10, "default") == "default"


class TestValidateAge:
    """Tests for validate_age function."""

    def test_valid_age(self):
        validate_age(0)  # Should not raise
        validate_age(25)  # Should not raise
        validate_age(150)  # Should not raise

    def test_negative_age(self):
        with pytest.raises(ValidationError, match="cannot be negative"):
            validate_age(-1)

    def test_excessive_age(self):
        with pytest.raises(ValidationError, match="cannot exceed 150"):
            validate_age(151)


class TestInsufficientFundsError:
    """Tests for InsufficientFundsError exception."""

    def test_attributes(self):
        error = InsufficientFundsError(100.0, 150.0)
        assert error.balance == 100.0
        assert error.amount == 150.0

    def test_message(self):
        error = InsufficientFundsError(100.0, 150.0)
        assert "150" in str(error)
        assert "100" in str(error)


class TestProcessPayment:
    """Tests for process_payment function."""

    def test_successful_payment(self):
        assert process_payment(100.0, 30.0) == 70.0
        assert process_payment(50.0, 50.0) == 0.0

    def test_insufficient_funds(self):
        with pytest.raises(InsufficientFundsError):
            process_payment(100.0, 150.0)


class TestReadConfig:
    """Tests for read_config function."""

    def test_all_keys_present(self):
        config = {"host": "localhost", "port": 8080, "debug": True}
        result = read_config(config, ["host", "port"])
        assert result == {"host": "localhost", "port": 8080}

    def test_missing_keys(self):
        config = {"host": "localhost"}
        with pytest.raises(KeyError) as exc_info:
            read_config(config, ["host", "port", "debug"])
        # The error should mention the missing keys
        assert "port" in str(exc_info.value) or "debug" in str(exc_info.value)
