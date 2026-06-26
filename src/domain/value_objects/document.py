import re
from dataclasses import dataclass

from src.domain.entities.document_type_entity import DocumentTypeEntity
from src.domain.exceptions.invalid_document_error import InvalidDocumentError


@dataclass(frozen=True)
class Document:
    number: str
    document_type: DocumentTypeEntity

    def __post_init__(self) -> None:
        self._validate_number()
        self._validate_format()

    def _validate_number(self) -> None:
        if not self.number or not self.number.strip():
            raise InvalidDocumentError(
                detail="document_number_empty",
                context={"number": self.number},
            )

    def _validate_format(self) -> None:
        if self.document_type.format_pattern:
            pattern = re.compile(self.document_type.format_pattern)
            if not pattern.match(self.number):
                raise InvalidDocumentError(
                    detail="document_number_invalid_format",
                    context={
                        "number": self.number,
                        "document_type": self.document_type.code,
                        "expected_pattern": self.document_type.format_pattern,
                    },
                )

    def __str__(self) -> str:
        return f"{self.document_type.code}-{self.number}"
