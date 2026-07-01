from src.domain.enums.week_day import WeekDay


def test_all_week_days_are_strings() -> None:
    assert all(isinstance(d.value, str) for d in WeekDay)


def test_values_are_lowercase() -> None:
    assert all(d.value.islower() for d in WeekDay)


def test_str_equals_value() -> None:
    assert all(str(d) == d.value for d in WeekDay)
