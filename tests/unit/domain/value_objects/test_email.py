import pytest

from src.domain.exceptions.domain_error import DomainError
from src.domain.exceptions.invalid_email_error import InvalidEmailError
from src.domain.value_objects.email import Email


@pytest.fixture
def entity() -> Email:
    return Email(value="juan.perez@example.com")


def test_value_is_stored(entity: Email) -> None:
    assert entity.value == "juan.perez@example.com"


def test_email_with_subdomain_is_valid() -> None:
    email = Email(value="user@mail.example.com")
    assert email.value == "user@mail.example.com"


def test_email_with_plus_is_valid() -> None:
    email = Email(value="user+tag@example.com")
    assert email.value == "user+tag@example.com"


def test_email_with_dots_in_local_is_valid() -> None:
    email = Email(value="first.last@example.com")
    assert email.value == "first.last@example.com"


def test_email_with_hyphen_in_domain_is_valid() -> None:
    email = Email(value="user@my-domain.com")
    assert email.value == "user@my-domain.com"


def test_value_is_lowercased() -> None:
    email = Email(value="Juan.Perez@Example.COM")
    assert email.value == "juan.perez@example.com"


def test_leading_and_trailing_spaces_are_stripped() -> None:
    email = Email(value="  juan.perez@example.com  ")
    assert email.value == "juan.perez@example.com"


def test_uppercase_and_spaces_are_normalized() -> None:
    email = Email(value="  JUAN@EXAMPLE.COM  ")
    assert email.value == "juan@example.com"


def test_is_immutable(entity: Email) -> None:
    with pytest.raises(Exception):
        entity.value = "other@example.com"


def test_empty_value_raises() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="")
    assert exc_info.value.detail == "email_empty"


def test_blank_value_raises() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="   ")
    assert exc_info.value.detail == "email_empty"


def test_empty_value_context_contains_email() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="")
    assert exc_info.value.context["email"] == ""


def test_email_exceeding_max_length_raises() -> None:
    long_email = "a" * 244 + "@example.com"
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value=long_email)
    assert exc_info.value.detail == "email_too_long"


def test_email_at_max_length_is_valid() -> None:
    valid_email = "a" * 242 + "@x.co"
    email = Email(value=valid_email)
    assert len(email.value) == 247


def test_email_without_at_raises() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="juanexample.com")
    assert exc_info.value.detail == "email_invalid_format"


def test_email_without_domain_raises() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="juan@")
    assert exc_info.value.detail == "email_invalid_format"


def test_email_without_tld_raises() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="juan@example")
    assert exc_info.value.detail == "email_invalid_format"


def test_email_with_spaces_raises() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="juan perez@example.com")
    assert exc_info.value.detail == "email_invalid_format"


def test_invalid_format_context_contains_email() -> None:
    with pytest.raises(InvalidEmailError) as exc_info:
        Email(value="notanemail")
    assert exc_info.value.context["email"] == "notanemail"


def test_invalid_format_is_caught_as_domain_error() -> None:
    with pytest.raises(DomainError):
        Email(value="notanemail")


def test_str_returns_value(entity: Email) -> None:
    assert str(entity) == "juan.perez@example.com"

