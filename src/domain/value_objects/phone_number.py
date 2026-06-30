from dataclasses import dataclass

import phonenumbers
from phonenumbers import NumberParseException, PhoneNumberFormat

from src.domain.exceptions import InvalidPhoneNumberError


@dataclass(frozen=True)
class PhoneNumber:
    value: str

    def __post_init__(self) -> None:
        normalized = self._parse_and_normalize(self.value)
        object.__setattr__(self, "value", normalized)

    def _parse_and_normalize(self, value: str) -> str:
        try:
            parsed = phonenumbers.parse(value, None)
        except NumberParseException:
            self._raise_invalid(self.value, "phone_number_invalid_format")

        if not phonenumbers.is_valid_number(parsed):
            self._raise_invalid(self.value, "phone_number_invalid_format")

        return phonenumbers.format_number(parsed, PhoneNumberFormat.E164)

    @staticmethod
    def _raise_invalid(value: str, detail) -> None:
        raise InvalidPhoneNumberError(detail=detail, context={"phone_number": value})
