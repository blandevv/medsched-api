from uuid import UUID

import pytest

from src.domain.entities.base_audit_entity import BaseAuditEntity


@pytest.fixture
def entity() -> BaseAuditEntity:
    return BaseAuditEntity()


def test_default_id_is_uuid(entity: BaseAuditEntity) -> None:
    assert isinstance(entity.id, UUID)


def test_ids_are_unique() -> None:
    entity1 = BaseAuditEntity()
    entity2 = BaseAuditEntity()
    assert entity1.id != entity2.id


def test_created_at_is_timezone_aware(entity: BaseAuditEntity) -> None:
    assert entity.created_at.tzinfo is not None
    assert entity.created_at.tzinfo.utcoffset(entity.created_at) is not None


def test_updated_at_is_timezone_aware(entity: BaseAuditEntity) -> None:
    assert entity.updated_at.tzinfo is not None
    assert entity.updated_at.tzinfo.utcoffset(entity.updated_at) is not None


def test_created_by_defaults_to_none(entity: BaseAuditEntity) -> None:
    assert entity.created_by is None


def test_updated_by_defaults_to_none(entity: BaseAuditEntity) -> None:
    assert entity.updated_by is None


def test_str_contains_id(entity: BaseAuditEntity) -> None:
    assert str(entity.id) in str(entity)
