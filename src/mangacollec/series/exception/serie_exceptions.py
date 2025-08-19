from mangacollec.core.exception.exception import MangaCollecException


class SerieNotFoundException(MangaCollecException):
    def __init__(self, serie_id: str):
        super().__init__(f"Serie with ID '{serie_id}' not found")


class SerieValidationException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Serie validation error: {message}")


class SerieAPIException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Serie API error: {message}")