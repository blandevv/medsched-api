from uuid import UUID

import pytest

from src.domain.entities.specialty_entity import SpecialtyEntity


@pytest.fixture
def entity() -> SpecialtyEntity:
    return SpecialtyEntity(
        code="CARD", name="Cardiology", default_duration_minutes=30, is_active=True
    )


def test_code_is_stored(entity: SpecialtyEntity) -> None:
    assert entity.code == "CARD"


def test_name_is_stored(entity: SpecialtyEntity) -> None:
    assert entity.name == "Cardiology"


def test_description_defaults_to_none(entity: SpecialtyEntity) -> None:
    assert entity.description is None


def test_is_active_defaults_to_true(entity: SpecialtyEntity) -> None:
    assert entity.is_active is True


def test_is_active_can_be_set_to_false() -> None:
    entity = SpecialtyEntity(
        code="CARD", name="Cardiology", default_duration_minutes=30, is_active=False
    )
    assert entity.is_active is False


def test_str_contains_id(entity: SpecialtyEntity) -> None:
    assert str(entity.id) in str(entity)


def test_default_id_is_uuid(entity: SpecialtyEntity) -> None:
    assert isinstance(entity.id, UUID)
