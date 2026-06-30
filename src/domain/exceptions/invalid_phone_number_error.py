from src.domain.exceptions.domain_error import DomainError


class InvalidPhoneNumberError(DomainError):
    def __init__(self, detail: str, context: dict | None = None) -> None:
        super().__init__(code="invalid_phone_number", detail=detail, context=context)
