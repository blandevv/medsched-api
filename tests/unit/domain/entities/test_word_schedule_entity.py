from uuid import UUID

import pytest

from src.domain.entities.work_schedule_entity import WorkScheduleEntity
from src.domain.enums.week_day import WeekDay


@pytest.fixture
def entity() -> WorkScheduleEntity:
    return WorkScheduleEntity(
        week_day=WeekDay.MONDAY,
        start_time="09:00",
        end_time="17:00",
        is_active=True,
    )


def test_week_day_is_stored(entity: WorkScheduleEntity) -> None:
    assert entity.week_day == WeekDay.MONDAY


def test_start_time_is_stored(entity: WorkScheduleEntity) -> None:
    assert entity.start_time == "09:00"


def test_end_time_is_stored(entity: WorkScheduleEntity) -> None:
    assert entity.end_time == "17:00"


def test_break_time_defaults_to_none(entity: WorkScheduleEntity) -> None:
    assert entity.break_start_time is None
    assert entity.end_break_time is None


def test_is_active_defaults_to_true(entity: WorkScheduleEntity) -> None:
    assert entity.is_active is True


def test_id_is_uuid(entity: WorkScheduleEntity) -> None:
    assert isinstance(entity.id, UUID)


def test_break_times_can_be_set(entity: WorkScheduleEntity) -> None:
    entity.break_start_time = "12:00"
    entity.end_break_time = "13:00"
    assert entity.break_start_time == "12:00"
    assert entity.end_break_time == "13:00"


def test_is_active_can_be_set(entity: WorkScheduleEntity) -> None:
    entity.is_active = False
    assert entity.is_active is False


def test_str_contains_id(entity: WorkScheduleEntity) -> None:
    assert str(entity).startswith("WorkScheduleEntity(id=")
