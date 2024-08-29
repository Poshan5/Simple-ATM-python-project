#test atm system
import pytest
from atm import validate_pin, check_balance, check_pin

def test_validate_pin_correct():
    try:
        validate_pin("8848", "8848")
    except ValueError:
        pytest.fail("validate_pin raised ValueError unexpectedly")

def test_validate_pin_incorrect():
    with pytest.raises(ValueError):
        validate_pin("8848", "1234")

def test_check_balance_sufficient():
    try:
        check_balance(1000, 500)
    except ValueError:
        pytest.fail("check_balance raised ValueError unexpectedly")

def test_check_balance_insufficient():
    with pytest.raises(ValueError):
        check_balance(1000, 1500)

def test_check_pin_match():
    try:
        check_pin("1234", "1234")
    except ValueError:
        pytest.fail("check_pin raised ValueError unexpectedly")

def test_check_pin_mismatch():
    with pytest.raises(ValueError):
        check_pin("1234", "5678")

