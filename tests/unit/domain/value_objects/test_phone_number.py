import pytest

from src.domain.value_objects import PhoneNumber
from src.domain.exceptions import InvalidPhoneNumberError


def test_valid_phone_number() -> None:
    phone = PhoneNumber("+573001234567")
    assert phone.value == "+573001234567"


def test_phone_number_without_country_code() -> None:
    with pytest.raises(InvalidPhoneNumberError):
        PhoneNumber("3001234567")


def test_phone_number_with_invalid_characters() -> None:
    with pytest.raises(InvalidPhoneNumberError):
        PhoneNumber("+57a001234567")


def test_phone_too_short() -> None:
    with pytest.raises(InvalidPhoneNumberError):
        PhoneNumber("+57123")
