from uuid import UUID

import pytest

from src.domain.entities.document_type_entity import DocumentTypeEntity
from src.domain.entities.role_entity import RoleEntity
from src.domain.entities.user_entity import UserEntity
from src.domain.enums.gender import Gender
from src.domain.value_objects import Document, Email, PersonName, PhoneNumber


@pytest.fixture
def document_type() -> DocumentTypeEntity:
    return DocumentTypeEntity(code="CC", name="Cedula de Ciudadania")


@pytest.fixture
def document(document_type: DocumentTypeEntity) -> Document:
    return Document(number="123456789", document_type=document_type)


@pytest.fixture
def role() -> RoleEntity:
    return RoleEntity(code="patient", name="Patient")


@pytest.fixture
def entity(role: RoleEntity, document: Document) -> UserEntity:
    return UserEntity(
        document=document,
        gender=Gender.MALE,
        first_name=PersonName(value="John"),
        first_last_name=PersonName(value="Doe"),
        email=Email(value="john.doe@example.com"),
        phone_number=PhoneNumber("+573001234567"),
        password_hash="hashed_password",
        role=role,
    )


def test_document_is_stored(entity: UserEntity, document: Document) -> None:
    assert entity.document == document


def test_gender_is_stored(entity: UserEntity) -> None:
    assert entity.gender == Gender.MALE


def test_first_name_is_stored(entity: UserEntity) -> None:
    assert entity.first_name == PersonName(value="John")


def test_first_last_name_is_stored(entity: UserEntity) -> None:
    assert entity.first_last_name == PersonName(value="Doe")


def test_email_is_stored(entity: UserEntity) -> None:
    assert entity.email == Email(value="john.doe@example.com")


def test_phone_number_is_stored(entity: UserEntity) -> None:
    assert entity.phone_number == PhoneNumber("+573001234567")


def test_password_hash_is_stored(entity: UserEntity) -> None:
    assert entity.password_hash == "hashed_password"


def test_role_is_stored(entity: UserEntity, role: RoleEntity) -> None:
    assert entity.role == role


def test_middle_name_defaults_to_none(entity: UserEntity) -> None:
    assert entity.middle_name is None


def test_second_last_name_defaults_to_none(entity: UserEntity) -> None:
    assert entity.second_last_name is None


def test_profile_picture_url_defaults_to_none(entity: UserEntity) -> None:
    assert entity.profile_picture_url is None


def test_is_active_defaults_to_true(entity: UserEntity) -> None:
    assert entity.is_active is True


def test_is_active_can_be_set_to_false(
    role: RoleEntity, document: Document
) -> None:
    user = UserEntity(
        document=document,
        gender=Gender.MALE,
        first_name=PersonName(value="John"),
        first_last_name=PersonName(value="Doe"),
        email=Email(value="john.doe@example.com"),
        phone_number=PhoneNumber("+573001234567"),
        password_hash="hashed_password",
        role=role,
        is_active=False,
    )
    assert user.is_active is False


def test_fullname_with_required_names_only(entity: UserEntity) -> None:
    assert entity.fullname == "John Doe"


def test_fullname_includes_middle_name(
    role: RoleEntity, document: Document
) -> None:
    user = UserEntity(
        document=document,
        gender=Gender.MALE,
        first_name=PersonName(value="John"),
        middle_name=PersonName(value="Paul"),
        first_last_name=PersonName(value="Doe"),
        email=Email(value="john.doe@example.com"),
        phone_number=PhoneNumber("+573001234567"),
        password_hash="hashed_password",
        role=role,
    )
    assert user.fullname == "John Paul Doe"


def test_fullname_includes_second_last_name(
    role: RoleEntity, document: Document
) -> None:
    user = UserEntity(
        document=document,
        gender=Gender.MALE,
        first_name=PersonName(value="John"),
        first_last_name=PersonName(value="Doe"),
        second_last_name=PersonName(value="Smith"),
        email=Email(value="john.doe@example.com"),
        phone_number=PhoneNumber("+573001234567"),
        password_hash="hashed_password",
        role=role,
    )
    assert user.fullname == "John Doe Smith"


def test_fullname_includes_all_names(
    role: RoleEntity, document: Document
) -> None:
    user = UserEntity(
        document=document,
        gender=Gender.MALE,
        first_name=PersonName(value="John"),
        middle_name=PersonName(value="Paul"),
        first_last_name=PersonName(value="Doe"),
        second_last_name=PersonName(value="Smith"),
        email=Email(value="john.doe@example.com"),
        phone_number=PhoneNumber("+573001234567"),
        password_hash="hashed_password",
        role=role,
    )
    assert user.fullname == "John Paul Doe Smith"


def test_inherits_uuid_id(entity: UserEntity) -> None:
    assert isinstance(entity.id, UUID)


def test_ids_are_unique(role: RoleEntity, document: Document) -> None:
    def make_user() -> UserEntity:
        return UserEntity(
            document=document,
            gender=Gender.MALE,
            first_name=PersonName(value="John"),
            first_last_name=PersonName(value="Doe"),
            email=Email(value="john.doe@example.com"),
            phone_number=PhoneNumber("+573001234567"),
            password_hash="hashed_password",
            role=role,
        )

    assert make_user().id != make_user().id


def test_str_contains_id(entity: UserEntity) -> None:
    assert str(entity.id) in str(entity)


def test_str_contains_fullname(entity: UserEntity) -> None:
    assert entity.fullname in str(entity)


def test_str_contains_email(entity: UserEntity) -> None:
    assert str(entity.email) in str(entity)


def test_str_contains_role_name(entity: UserEntity) -> None:
    assert entity.role.name in str(entity)


def test_str_contains_is_active(entity: UserEntity) -> None:
    assert str(entity.is_active) in str(entity)


def test_str_label(entity: UserEntity) -> None:
    assert str(entity).startswith("UserEntity(")
