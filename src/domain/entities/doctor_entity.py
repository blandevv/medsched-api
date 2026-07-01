from dataclasses import dataclass, field

from src.domain.entities.specialty_entity import SpecialtyEntity
from src.domain.entities.user_entity import UserEntity
from src.domain.entities.work_schedule_entity import WorkScheduleEntity


@dataclass(kw_only=True)
class DoctorEntity(UserEntity):
    specialty: SpecialtyEntity
    work_schedules: list[WorkScheduleEntity] = field(default_factory=list)

    def __str__(self) -> str:
        return (
            f"DoctorEntity("
            f"id={self.id}, "
            f"fullname={self.fullname}, "
            f"specialty={self.specialty.name}, "
            f"work_schedules={[str(ws) for ws in self.work_schedules]}, "
            f"is_active={self.is_active})"
        )
