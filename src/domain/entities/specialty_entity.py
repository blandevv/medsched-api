from dataclasses import dataclass

from src.domain.entities.base_audit_entity import BaseAuditEntity


@dataclass(kw_only=True)
class SpecialtyEntity(BaseAuditEntity):
    code: str
    name: str
    default_duration_minutes: int
    description: str | None = None
    is_active: bool = True

    def __str__(self) -> str:
        return (
            f"SpecialtyEntity("
            f"id={self.id}, "
            f"code={self.code}, "
            f"name={self.name}, "
            f"default_duration_minutes={self.default_duration_minutes}, "
            f"description={self.description}, "
            f"is_active={self.is_active})"
        )
