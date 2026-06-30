from dataclasses import dataclass

from src.domain.entities.base_audit_entity import BaseAuditEntity
from src.domain.entities.role_entity import RoleEntity
from src.domain.enums.gender import Gender
from src.domain.value_objects import Document, Email, PersonName, PhoneNumber


@dataclass(kw_only=True)
class UserEntity(BaseAuditEntity):
    document: Document
    gender: Gender
    first_name: PersonName
    first_last_name: PersonName
    email: Email
    phone_number: PhoneNumber
    password_hash: str
    role: RoleEntity

    middle_name: PersonName | None = None
    second_last_name: PersonName | None = None
    profile_picture_url: str | None = None
    is_active: bool = True

    @property
    def fullname(self) -> str:
        names = (
            self.first_name,
            self.middle_name,
            self.first_last_name,
            self.second_last_name,
        )
        return " ".join(map(str, filter(None, names)))

    def __str__(self) -> str:
        return (
            f"UserEntity("
            f"id={self.id}, "
            f"fullname={self.fullname}, "
            f"email={self.email}, "
            f"role={self.role.name}, "
            f"is_active={self.is_active})"
        )
