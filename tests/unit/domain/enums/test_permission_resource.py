from src.domain.enums.permission_resource import PermissionResource


def test_all_resources_are_strings() -> None:
    assert all(isinstance(resource.value, str) for resource in PermissionResource)


def test_values_are_lowercase() -> None:
    assert all(resource.value.islower() for resource in PermissionResource)


def test_str_equals_value() -> None:
    assert all(str(resource) == resource.value for resource in PermissionResource)
