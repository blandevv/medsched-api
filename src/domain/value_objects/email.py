import re
from dataclasses import dataclass

from src.domain.exceptions.invalid_email_error import InvalidEmailError

_EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")
_MAX_LENGTH = 254


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()
        object.__setattr__(self, "value", normalized)
        self._validate(normalized)

    def __str__(self) -> str:
        return self.value

    def _validate(self, value: str) -> None:
        if not value:
            self._raise_invalid(value, "email_empty")
        if len(value) > _MAX_LENGTH:
            self._raise_invalid(value, "email_too_long")
        if not _EMAIL_PATTERN.fullmatch(value):
            self._raise_invalid(value, "email_invalid_format")

    @staticmethod
    def _raise_invalid(value: str, detail: str) -> None:
        raise InvalidEmailError(detail=detail, context={"email": value})
