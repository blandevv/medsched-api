from src.domain.exceptions.domain_error import DomainError


class InvalidEmailError(DomainError):
    def __init__(self, detail: str, context: dict | None = None) -> None:
        super().__init__(code="invalid_email", detail=detail, context=context)
