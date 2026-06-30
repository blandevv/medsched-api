from dataclasses import dataclass

from src.domain.entities.base_audit_entity import BaseAuditEntity


@dataclass(kw_only=True)
class SpecialtyEntity(BaseAuditEntity):
    code: str
    name: str
    description: str | None = None
    is_active: bool = True

    def __str__(self) -> str:
        return (
            f"SpecialtyEntity("
            f"id={self.id}, "
            f"code={self.code}, "
            f"name={self.name}, "
            f"description={self.description}, "
            f"is_active={self.is_active})"
        )
