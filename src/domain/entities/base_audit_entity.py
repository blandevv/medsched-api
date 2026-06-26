from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass
class BaseAuditEntity:
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    created_by: UUID | None = None
    updated_by: UUID | None = None

    def __str__(self) -> str:
        return (
            f"BaseAuditEntity("
            f"id={self.id}, "
            f"created_at={self.created_at}, "
            f"updated_at={self.updated_at}, "
            f"created_by={self.created_by}, "
            f"updated_by={self.updated_by})"
        )
