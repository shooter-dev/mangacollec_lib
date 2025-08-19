from mangacollec.core.exception.exception import MangaCollecException


class PublisherNotFoundException(MangaCollecException):
    def __init__(self, publisher_id: str):
        super().__init__(f"Publisher with ID '{publisher_id}' not found")


class PublisherValidationException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Publisher validation error: {message}")


class PublisherAPIException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Publisher API error: {message}")