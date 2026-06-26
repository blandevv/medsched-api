from dataclasses import dataclass

from src.domain.entities.base_audit_entity import BaseAuditEntity


@dataclass(kw_only=True)
class DocumentTypeEntity(BaseAuditEntity):
    code: str
    name: str
    is_active: bool = True

    def __str__(self) -> str:
        return (
            f"DocumentTypeEntity("
            f"id={self.id}, "
            f"code={self.code}, "
            f"name={self.name}, "
            f"is_active={self.is_active})"
        )
