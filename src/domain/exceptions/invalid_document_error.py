from src.domain.exceptions.domain_error import DomainError


class InvalidDocumentError(DomainError):
    def __init__(self, message: str, context: dict | None = None) -> None:
        super().__init__(code="invalid_document", message=message, context=context)
