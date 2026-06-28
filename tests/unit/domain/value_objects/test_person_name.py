import pytest

from src.domain.exceptions.invalid_person_name_error import InvalidPersonNameError
from src.domain.value_objects.person_name import PersonName


@pytest.fixture
def entity() -> PersonName:
    return PersonName(value="John Doe")


def test_value_is_stored(entity: PersonName) -> None:
    assert entity.value == "John Doe"


def test_single_word_name_is_valid() -> None:
    name = PersonName(value="John")
    assert name.value == "John"


def test_name_with_accent_is_valid() -> None:
    name = PersonName(value="José")
    assert name.value == "José"


def test_name_with_hyphen_is_valid() -> None:
    name = PersonName(value="Mary-Jane")
    assert name.value == "Mary-Jane"


def test_name_with_apostrophe_is_valid() -> None:
    name = PersonName(value="O'Connor")
    assert name.value == "O'Connor"


def test_value_is_title_cased() -> None:
    name = PersonName(value="john doe")
    assert name.value == "John Doe"


def test_extra_spaces_are_normalized() -> None:
    name = PersonName(value="  John   Doe  ")
    assert name.value == "John Doe"


def test_mixed_case_is_normalized() -> None:
    name = PersonName(value="jOhN dOe")
    assert name.value == "John Doe"


def test_is_inmutable(entity: PersonName) -> None:
    with pytest.raises(Exception):
        entity.value = "Jane Doe"


def test_empty_value_raises() -> None:
    with pytest.raises(InvalidPersonNameError) as exc_info:
        PersonName(value="")
    assert exc_info.value.detail == "name_empty"


def test_invalid_format_raises() -> None:
    with pytest.raises(InvalidPersonNameError) as exc_info:
        PersonName(value="John123")
    assert exc_info.value.detail == "name_invalid_format"


def test_str_returns_value(entity: PersonName) -> None:
    assert str(entity) == "John Doe"
