from dataclasses import dataclass, field

from src.domain.entities.base_audit_entity import BaseAuditEntity
from src.domain.entities.permission_entity import PermissionEntity


@dataclass(kw_only=True)
class RoleEntity(BaseAuditEntity):
    code: str
    name: str
    description: str | None = None
    permissions: list[PermissionEntity] = field(default_factory=list)
    is_active: bool = True

    def __str__(self) -> str:
        return (
            f"RoleEntity("
            f"id={self.id}, "
            f"code={self.code}, "
            f"name={self.name}, "
            f"description={self.description}, "
            f"permissions={self.permissions}, "
            f"is_active={self.is_active})"
        )
