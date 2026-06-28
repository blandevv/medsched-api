from src.domain.exceptions.domain_error import DomainError


class InvalidPersonNameError(DomainError):
    def __init__(self, detail: str, context: dict | None = None) -> None:
        super().__init__(code="invalid_person_name", detail=detail, context=context)
