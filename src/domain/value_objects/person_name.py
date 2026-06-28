import re
from dataclasses import dataclass

from src.domain.exceptions.invalid_person_name_error import InvalidPersonNameError

_NAME_PATTERN = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ'-]+(?: [A-Za-zÁÉÍÓÚÜÑáéíóúüñ'-]+)*")


@dataclass(frozen=True)
class PersonName:
    value: str

    def __post_init__(self) -> None:
        normalized = " ".join(self.value.split()).title()

        if not normalized:
            self._raise_invalid(self.value, "name_empty")
        if not _NAME_PATTERN.fullmatch(normalized):
            self._raise_invalid(self.value, "name_invalid_format")
        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value

    @staticmethod
    def _raise_invalid(value: str, detail: str) -> None:
        raise InvalidPersonNameError(detail=detail, context={"name": value})
