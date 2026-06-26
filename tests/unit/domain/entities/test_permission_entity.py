from uuid import UUID

import pytest

from src.domain.entities.permission_entity import PermissionEntity
from src.domain.enums.permission_action import PermissionAction
from src.domain.enums.permission_resource import PermissionResource


@pytest.fixture
def entity() -> PermissionEntity:
    return PermissionEntity(
        resource=PermissionResource.USERS,
        action=PermissionAction.READ,
        name="Read users",
    )


def test_resource_is_store(entity: PermissionEntity) -> None:
    assert entity.resource == PermissionResource.USERS


def test_action_is_stored(entity: PermissionEntity) -> None:
    assert entity.action == PermissionAction.READ


def test_name_is_stored(entity: PermissionEntity) -> None:
    assert entity.name == "Read users"


def test_description_defaults_to_none(entity: PermissionEntity) -> None:
    assert entity.description is None


def test_description_can_be_set() -> None:
    entity = PermissionEntity(
        resource=PermissionResource.USERS,
        action=PermissionAction.READ,
        name="Read users",
        description="Allows reading user data",
    )
    assert entity.description == "Allows reading user data"


def test_is_active_defaults_to_true(entity: PermissionEntity) -> None:
    assert entity.is_active is True


def test_is_active_can_be_set_to_false() -> None:
    entity = PermissionEntity(
        resource=PermissionResource.USERS,
        action=PermissionAction.READ,
        name="Read users",
        is_active=False,
    )
    assert entity.is_active is False


def test_code_format(entity: PermissionEntity) -> None:
    assert entity.code == f"{entity.resource.value}.{entity.action.value}"


def test_code_uses_resource_and_action_values(entity: PermissionEntity) -> None:
    assert (
        entity.code == f"{PermissionResource.USERS.value}.{PermissionAction.READ.value}"
    )


def test_code_is_not_stored_as_field(entity: PermissionEntity) -> None:
    assert "code" not in entity.__dataclass_fields__


def test_inherits_uuid_id(entity: PermissionEntity) -> None:
    assert isinstance(entity.id, UUID)


def test_ids_are_unique() -> None:
    entity1 = PermissionEntity(
        resource=PermissionResource.USERS,
        action=PermissionAction.READ,
        name="Read users",
    )
    entity2 = PermissionEntity(
        resource=PermissionResource.USERS,
        action=PermissionAction.CREATE,
        name="Write users",
    )
    assert entity1.id != entity2.id


def test_created_at_is_timezone_aware(entity: PermissionEntity) -> None:
    assert entity.created_at.tzinfo is not None
    assert entity.created_at.tzinfo.utcoffset(entity.created_at) is not None


def test_updated_at_is_timezone_aware(entity: PermissionEntity) -> None:
    assert entity.updated_at.tzinfo is not None
    assert entity.updated_at.tzinfo.utcoffset(entity.updated_at) is not None


def test_created_by_defaults_to_none(entity: PermissionEntity) -> None:
    assert entity.created_by is None


def test_updated_by_defaults_to_none(entity: PermissionEntity) -> None:
    assert entity.updated_by is None


def test_str_contains_id(entity: PermissionEntity) -> None:
    assert str(entity.id) in str(entity)


def test_str_contains_resource(entity: PermissionEntity) -> None:
    assert str(entity.resource) in str(entity)
