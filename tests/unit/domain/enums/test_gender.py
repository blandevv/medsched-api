from src.domain.enums.gender import Gender


def test_all_genders_are_strings() -> None:
    assert all(isinstance(g.value, str) for g in Gender)


def test_values_are_lowercase() -> None:
    assert all(g.value.islower() for g in Gender)


def test_str_equals_value() -> None:
    assert all(str(g) == g.value for g in Gender)
