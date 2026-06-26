from dataclasses import dataclass

from src.domain.entities.base_audit_entity import BaseAuditEntity
from src.domain.enums.permission_action import PermissionAction
from src.domain.enums.permission_resource import PermissionResource


@dataclass(kw_only=True)
class PermissionEntity(BaseAuditEntity):
    resource: PermissionResource
    action: PermissionAction
    name: str
    description: str | None = None
    is_active: bool = True

    @property
    def code(self) -> str:
        return f"{self.resource.value}.{self.action.value}"

    def __str__(self) -> str:
        return (
            f"PermissionEntity("
            f"id={self.id}, "
            f"resource={self.resource}, "
            f"action={self.action}, "
            f"name={self.name}, "
            f"description={self.description}, "
            f"is_active={self.is_active})"
        )
