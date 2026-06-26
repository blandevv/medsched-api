from uuid import UUID

import pytest

from src.domain.entities.document_type_entity import DocumentTypeEntity


@pytest.fixture
def entity() -> DocumentTypeEntity:
    return DocumentTypeEntity(code="DNI", name="National ID")


def test_code_is_stored(entity: DocumentTypeEntity) -> None:
    assert entity.code == "DNI"


def test_name_is_stored(entity: DocumentTypeEntity) -> None:
    assert entity.name == "National ID"


def test_is_active_defaults_to_true(entity: DocumentTypeEntity) -> None:
    assert entity.is_active is True


def test_is_active_can_be_set_to_false() -> None:
    entity = DocumentTypeEntity(code="DNI", name="National ID", is_active=False)
    assert entity.is_active is False


def test_inherits_uuid_id(entity: DocumentTypeEntity) -> None:
    assert isinstance(entity.id, UUID)


def test_ids_are_unique() -> None:
    entity1 = DocumentTypeEntity(code="DNI", name="National ID")
    entity2 = DocumentTypeEntity(code="PASSPORT", name="Passport")
    assert entity1.id != entity2.id


def teset_created_at_is_timezone_aware(entity: DocumentTypeEntity) -> None:
    assert entity.created_at.tzinfo is not None
    assert entity.created_at.tzinfo.utcoffset(entity.created_at) is not None


def test_updated_at_is_timezone_aware(entity: DocumentTypeEntity) -> None:
    assert entity.updated_at.tzinfo is not None
    assert entity.updated_at.tzinfo.utcoffset(entity.updated_at) is not None


def test_str_contains_code_and_name(entity: DocumentTypeEntity) -> None:
    assert entity.code in str(entity)
    assert entity.name in str(entity)


def test_format_pattern_defaults_to_none(entity: DocumentTypeEntity) -> None:
    assert entity.format_pattern is None


def test_format_pattern_can_be_set() -> None:
    format_pattern = r"^\d{8}$"

    entity = DocumentTypeEntity(
        code="DNI", name="National ID", format_pattern=format_pattern
    )
    assert entity.format_pattern == format_pattern
