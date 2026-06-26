import pytest

from src.domain.exceptions.domain_error import DomainError
from src.domain.exceptions.invalid_document_error import InvalidDocumentError


@pytest.fixture
def entity() -> InvalidDocumentError:
    return InvalidDocumentError(
        detail="Invalid document", context={"document": "12345678"}
    )


def test_code_is_fixed(entity: InvalidDocumentError) -> None:
    assert entity.code == "invalid_document"


def test_detail_is_stored(entity: InvalidDocumentError) -> None:
    assert entity.detail == "Invalid document"


def test_is_domain_error(entity: InvalidDocumentError) -> None:
    assert issubclass(type(entity), DomainError)


def test_can_be_raised_and_caught_as_domain_error() -> None:
    with pytest.raises(DomainError):
        raise InvalidDocumentError(detail="Invalid document")
