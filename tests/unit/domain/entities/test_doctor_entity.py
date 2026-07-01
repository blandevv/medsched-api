import pytest

from src.domain.entities.doctor_entity import DoctorEntity
from src.domain.entities.document_type_entity import DocumentTypeEntity
from src.domain.entities.role_entity import RoleEntity
from src.domain.entities.specialty_entity import SpecialtyEntity
from src.domain.entities.work_schedule_entity import WorkScheduleEntity
from src.domain.enums.gender import Gender
from src.domain.enums.week_day import WeekDay
from src.domain.value_objects import Document, Email, PersonName, PhoneNumber


@pytest.fixture
def document_type() -> DocumentTypeEntity:
    return DocumentTypeEntity(code="CC", name="Cedula de Ciudadania")


@pytest.fixture
def document(document_type: DocumentTypeEntity) -> Document:
    return Document(number="123456789", document_type=document_type)


@pytest.fixture
def role() -> RoleEntity:
    return RoleEntity(code="doctor", name="Doctor")


@pytest.fixture
def specialty() -> SpecialtyEntity:
    return SpecialtyEntity(code="CARD", name="Cardiology", default_duration_minutes=30)


@pytest.fixture
def work_schedule() -> WorkScheduleEntity:
    return WorkScheduleEntity(
        week_day=WeekDay.MONDAY,
        start_time="09:00",
        end_time="17:00",
    )


@pytest.fixture
def entity(
    role: RoleEntity, document: Document, specialty: SpecialtyEntity
) -> DoctorEntity:
    return DoctorEntity(
        document=document,
        gender=Gender.MALE,
        first_name=PersonName(value="John"),
        first_last_name=PersonName(value="Doe"),
        email=Email(value="john.doe@example.com"),
        phone_number=PhoneNumber("+573001234567"),
        password_hash="hashed_password",
        role=role,
        specialty=specialty,
    )


def test_specialty_is_stored(entity: DoctorEntity, specialty: SpecialtyEntity) -> None:
    assert entity.specialty == specialty


def test_work_schedules_defaults_to_empty_list(entity: DoctorEntity) -> None:
    assert entity.work_schedules == []


def test_work_schedules_can_be_set(
    role: RoleEntity,
    document: Document,
    specialty: SpecialtyEntity,
    work_schedule: WorkScheduleEntity,
) -> None:
    doctor = DoctorEntity(
        document=document,
        gender=Gender.MALE,
        first_name=PersonName(value="John"),
        first_last_name=PersonName(value="Doe"),
        email=Email(value="john.doe@example.com"),
        phone_number=PhoneNumber("+573001234567"),
        password_hash="hashed_password",
        role=role,
        specialty=specialty,
        work_schedules=[work_schedule],
    )
    assert doctor.work_schedules == [work_schedule]


def test_str_label(entity: DoctorEntity) -> None:
    assert str(entity).startswith("DoctorEntity(")


def test_str_contains_id(entity: DoctorEntity) -> None:
    assert str(entity.id) in str(entity)


def test_str_contains_fullname(entity: DoctorEntity) -> None:
    assert entity.fullname in str(entity)


def test_str_contains_specialty_name(
    entity: DoctorEntity, specialty: SpecialtyEntity
) -> None:
    assert specialty.name in str(entity)


def test_str_contains_is_active(entity: DoctorEntity) -> None:
    assert str(entity.is_active) in str(entity)
