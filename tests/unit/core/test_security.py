import jwt
import pytest

from src.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)


def test_hash_password_returns_different_value() -> None:
    password = "my-password"
    hashed_password = hash_password(password)

    assert hashed_password != password


def test_verify_password_returns_true_for_correct_password() -> None:
    password = "my-password"
    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password) is True


def test_verify_password_returns_false_for_incorrect_password() -> None:
    password = "my-password"
    hashed_password = hash_password(password)

    assert verify_password("wrong-password", hashed_password) is False


def test_create_access_token_contains_subject() -> None:
    token = create_access_token(subject=123)
    payload = decode_token(token)

    assert payload["sub"] == "123"


def test_create_access_token_contains_type() -> None:
    token = create_access_token(subject=123)
    payload = decode_token(token)

    assert payload["type"] == "access"


def test_create_access_token_contains_extra_data() -> None:
    token = create_access_token(subject=123, extra_data={"role": "admin"})
    payload = decode_token(token)

    assert payload["role"] == "admin"


def test_create_refresh_token_contains_type() -> None:
    token = create_refresh_token(subject=123)
    payload = decode_token(token)

    assert payload["type"] == "refresh"


def test_decode_token_returns_payload() -> None:
    token = create_access_token(subject=123)
    payload = decode_token(token)

    assert payload["sub"] == "123"
    assert payload["type"] == "access"


def test_decode_token_raises_invalid_token_error() -> None:
    with pytest.raises(jwt.InvalidTokenError):
        decode_token("invalid-token")


def test_create_access_token_contains_issuer() -> None:
    token = create_access_token(subject=123)
    payload = decode_token(token)

    assert payload["iss"] == "medsched-api"


def test_create_access_token_contains_issued_at() -> None:
    token = create_access_token(subject=123)
    payload = decode_token(token)

    assert "iat" in payload
