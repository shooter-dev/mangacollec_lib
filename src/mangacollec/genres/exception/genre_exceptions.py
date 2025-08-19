from mangacollec.core.exception.exception import MangaCollecException


class GenreNotFoundException(MangaCollecException):
    def __init__(self, genre_id: str):
        super().__init__(f"Genre with ID '{genre_id}' not found")


class GenreValidationException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Genre validation error: {message}")


class GenreAPIException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Genre API error: {message}")