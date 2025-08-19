from mangacollec.core.exception.exception import MangaCollecException


class KindNotFoundException(MangaCollecException):
    def __init__(self, kind_id: str):
        super().__init__(f"Kind with ID '{kind_id}' not found")


class KindValidationException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Kind validation error: {message}")


class KindAPIException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Kind API error: {message}")