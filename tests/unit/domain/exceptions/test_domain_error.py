import pytest

from src.domain.exceptions.domain_error import DomainError


@pytest.fixture
def entity() -> DomainError:
    return DomainError(code="test_code", detail="Test detail", context={"key": "value"})


def test_code_is_stored(entity: DomainError) -> None:
    assert entity.code == "test_code"


def test_detail_is_stored(entity: DomainError) -> None:
    assert entity.detail == "Test detail"


def test_context_is_stored(entity: DomainError) -> None:
    assert entity.context == {"key": "value"}


def test_is_a_exception(entity: DomainError) -> None:
    assert isinstance(entity, Exception)
