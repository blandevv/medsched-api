from src.domain.enums.permission_action import PermissionAction


def test_all_actions_are_strings() -> None:
    assert all(isinstance(action.value, str) for action in PermissionAction)


def test_values_are_lowercase() -> None:
    assert all(action.value.islower() for action in PermissionAction)


def test_str_equals_value() -> None:
    assert all(str(action) == action.value for action in PermissionAction)
