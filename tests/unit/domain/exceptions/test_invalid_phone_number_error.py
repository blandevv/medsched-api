import pytest

from src.domain.exceptions.domain_error import DomainError
from src.domain.exceptions import InvalidPhoneNumberError


@pytest.fixture
def entity() -> InvalidPhoneNumberError:
    return InvalidPhoneNumberError(
        detail="phone_number_invalid_format", context={"phone_number": "abc"}
    )


def test_code_is_fixed(entity: InvalidPhoneNumberError) -> None:
    assert entity.code == "invalid_phone_number"


def test_detail_is_stored(entity: InvalidPhoneNumberError) -> None:
    assert entity.detail == "phone_number_invalid_format"


def test_is_domain_error(entity: InvalidPhoneNumberError) -> None:
    assert issubclass(type(entity), DomainError)


def test_can_be_raised_and_caught_as_domain_error() -> None:
    with pytest.raises(DomainError):
        raise InvalidPhoneNumberError(detail="phone_number_invalid_format")
