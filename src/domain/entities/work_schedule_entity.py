from dataclasses import dataclass
from datetime import time

from src.domain.entities.base_audit_entity import BaseAuditEntity
from src.domain.enums.week_day import WeekDay


@dataclass(kw_only=True)
class WorkScheduleEntity(BaseAuditEntity):
    week_day: WeekDay
    start_time: time
    end_time: time
    is_active: bool = True
    break_start_time: time | None = None
    end_break_time: time | None = None

    def __str__(self) -> str:
        return (
            f"WorkScheduleEntity("
            f"id={self.id}, "
            f"week_day={self.week_day}, "
            f"start_time={self.start_time}, "
            f"end_time={self.end_time}, "
            f"break_start_time={self.break_start_time}, "
            f"end_break_time={self.end_break_time}, "
            f"is_active={self.is_active})"
        )
