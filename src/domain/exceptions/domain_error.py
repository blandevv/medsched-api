class DomainError(Exception):
    def __init__(self, code: str, detail: str, context: dict | None = None) -> None:
        self.code = code
        self.detail = detail
        self.context = context or {}

        super().__init__(self.detail)
