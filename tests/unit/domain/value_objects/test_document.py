import pytest

from src.domain.entities.document_type_entity import DocumentTypeEntity
from src.domain.exceptions.domain_error import DomainError
from src.domain.exceptions.invalid_document_error import InvalidDocumentError
from src.domain.value_objects.document import Document


@pytest.fixture
def document_type() -> DocumentTypeEntity:
    return DocumentTypeEntity(code="DNI", name="National ID", format_pattern=r"^\d{8}$")


@pytest.fixture
def document_type_no_pattern() -> DocumentTypeEntity:
    return DocumentTypeEntity(code="PP", name="Passport")


@pytest.fixture
def entity(document_type: DocumentTypeEntity) -> Document:
    return Document(number="12345678", document_type=document_type)


def test_number_is_stored(entity: Document) -> None:
    assert entity.number == "12345678"


def test_document_type_is_stored(
    entity: Document, document_type: DocumentTypeEntity
) -> None:
    assert entity.document_type == document_type


def test_valid_document_without_pattern(
    document_type_no_pattern: DocumentTypeEntity,
) -> None:
    document = Document(number="A1234567", document_type=document_type_no_pattern)
    assert document.number == "A1234567"
    assert document.document_type == document_type_no_pattern


def test_is_inmutable(entity: Document) -> None:
    with pytest.raises(Exception):
        entity.number = "87654321"


def test_empty_number_raises_invalid_document_error(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(InvalidDocumentError) as exc_info:
        Document(number="", document_type=document_type)
    assert exc_info.value.detail == "document_number_empty"
    assert exc_info.value.context == {"number": ""}


def test_blank_number_raises_invalid_document_error(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(InvalidDocumentError) as exc_info:
        Document(number="   ", document_type=document_type)
    assert exc_info.value.detail == "document_number_empty"
    assert exc_info.value.context == {"number": "   "}


def test_empty_number_context_contains_number(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(InvalidDocumentError) as exc_info:
        Document(number="", document_type=document_type)
    assert exc_info.value.context["number"] == ""


def test_str_format(entity: Document) -> None:
    assert str(entity) == "DNI-12345678"


def test_invalid_format_raises_invalid_document_error(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(InvalidDocumentError) as exc_info:
        Document(number="ABC", document_type=document_type)
    assert exc_info.value.detail == "document_number_invalid_format"


def test_invalid_format_context_contains_number(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(InvalidDocumentError) as exc_info:
        Document(number="ABC", document_type=document_type)
    assert exc_info.value.context["number"] == "ABC"


def test_invalid_format_context_contains_document_type(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(InvalidDocumentError) as exc_info:
        Document(number="ABC", document_type=document_type)
    assert exc_info.value.context["document_type"] == "DNI"


def test_invalid_format_context_contains_expected_pattern(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(InvalidDocumentError) as exc_info:
        Document(number="ABC", document_type=document_type)
    assert exc_info.value.context["expected_pattern"] == r"^\d{8}$"


def test_invalid_format_is_caught_as_domain_error(
    document_type: DocumentTypeEntity,
) -> None:
    with pytest.raises(DomainError):
        Document(number="ABC", document_type=document_type)
