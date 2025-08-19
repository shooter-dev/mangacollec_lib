from mangacollec.core.exception.exception import MangaCollecException


class EditionNotFoundException(MangaCollecException):
    def __init__(self, edition_id: str):
        super().__init__(f"Edition with ID '{edition_id}' not found")


class EditionValidationException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Edition validation error: {message}")


class EditionAPIException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Edition API error: {message}")