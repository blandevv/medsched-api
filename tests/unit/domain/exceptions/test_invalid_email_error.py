import pytest

from src.domain.exceptions.domain_error import DomainError
from src.domain.exceptions.invalid_email_error import InvalidEmailError


@pytest.fixture
def entity() -> InvalidEmailError:
    return InvalidEmailError(detail="Invalid email", context={"email": "invalid@"})


def test_code_is_fixed(entity: InvalidEmailError) -> None:
    assert entity.code == "invalid_email"


def test_detail_is_stored(entity: InvalidEmailError) -> None:
    assert entity.detail == "Invalid email"


def test_is_domain_error(entity: InvalidEmailError) -> None:
    assert issubclass(type(entity), DomainError)


def test_can_be_raised_and_caught_as_domain_error() -> None:
    with pytest.raises(DomainError):
        raise InvalidEmailError(detail="Invalid email")
