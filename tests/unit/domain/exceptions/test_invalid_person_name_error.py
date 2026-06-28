import pytest

from src.domain.exceptions.domain_error import DomainError
from src.domain.exceptions.invalid_person_name_error import InvalidPersonNameError


@pytest.fixture
def entity() -> InvalidPersonNameError:
    return InvalidPersonNameError(
        detail="Invalid person name", context={"name": "John Doe"}
    )


def test_code_is_fixed(entity: InvalidPersonNameError) -> None:
    assert entity.code == "invalid_person_name"


def test_detail_is_stored(entity: InvalidPersonNameError) -> None:
    assert entity.detail == "Invalid person name"


def test_is_domain_error(entity: InvalidPersonNameError) -> None:
    assert issubclass(type(entity), DomainError)


def test_can_be_raised_and_caught_as_domain_error() -> None:
    with pytest.raises(DomainError):
        raise InvalidPersonNameError(detail="Invalid person name")
