from uuid import UUID

import pytest

from src.domain.entities.permission_entity import PermissionEntity
from src.domain.entities.role_entity import RoleEntity
from src.domain.enums.permission_action import PermissionAction
from src.domain.enums.permission_resource import PermissionResource


@pytest.fixture
def permission() -> PermissionEntity:
    return PermissionEntity(
        resource=PermissionResource.USERS,
        action=PermissionAction.READ,
        name="Read users",
    )


@pytest.fixture
def entity() -> RoleEntity:
    return RoleEntity(
        code="admin",
        name="Administrator",
    )


def test_code_is_stored(entity: RoleEntity) -> None:
    assert entity.code == "admin"


def test_name_is_stored(entity: RoleEntity) -> None:
    assert entity.name == "Administrator"


def test_description_defaults_to_none(entity: RoleEntity) -> None:
    assert entity.description is None


def test_description_can_be_set() -> None:
    description = "Full access to the system"
    entity = RoleEntity(code="ADMIN", name="Administrator", description=description)
    assert entity.description == description


def test_is_active_defaults_to_true(entity: RoleEntity) -> None:
    assert entity.is_active is True


def test_is_active_can_be_set_to_false() -> None:
    entity = RoleEntity(code="ADMIN", name="Administrator", is_active=False)
    assert entity.is_active is False


def test_permissions_defaults_to_empty_list(entity: RoleEntity) -> None:
    assert entity.permissions == []


def test_permissions_default_is_not_shared() -> None:
    entity1 = RoleEntity(code="A", name="Role A")
    entity2 = RoleEntity(code="B", name="Role B")

    entity1.permissions.append(
        PermissionEntity(
            resource=PermissionResource.USERS,
            action=PermissionAction.READ,
            name="Read users",
        )
    )

    assert entity2.permissions == []


def test_permissions_can_be_set(permission: PermissionEntity) -> None:
    entity = RoleEntity(code="ADMIN", name="Administrator", permissions=[permission])
    assert len(entity.permissions) == 1
    assert entity.permissions[0] == permission


def test_permission_contains_permission_entities(permission: PermissionEntity) -> None:
    entity = RoleEntity(code="ADMIN", name="Administrator", permissions=[permission])
    assert all(isinstance(p, PermissionEntity) for p in entity.permissions)


def test_inherits_uuid_id(entity: RoleEntity) -> None:
    assert isinstance(entity.id, UUID)


def test_ids_are_unique() -> None:
    entity1 = RoleEntity(code="A", name="Role A")
    entity2 = RoleEntity(code="B", name="Role B")
    assert entity1.id != entity2.id


def test_created_at_is_timezone_aware(entity: RoleEntity) -> None:
    assert entity.created_at.tzinfo is not None


def test_updated_at_is_timezone_aware(entity: RoleEntity) -> None:
    assert entity.updated_at.tzinfo is not None


def test_created_by_defaults_to_none(entity: RoleEntity) -> None:
    assert entity.created_by is None


def test_updated_by_defaults_to_none(entity: RoleEntity) -> None:
    assert entity.updated_by is None


def test_str_contains_id(entity: RoleEntity) -> None:
    assert str(entity.id) in str(entity)


def test_str_contains_code(entity: RoleEntity) -> None:
    assert entity.code in str(entity)


def test_str_contains_name(entity: RoleEntity) -> None:
    assert entity.name in str(entity)


def test_str_contains_is_active(entity: RoleEntity) -> None:
    assert str(entity.is_active) in str(entity)


def test_str_label(entity: RoleEntity) -> None:
    assert str(entity).startswith("RoleEntity(")
