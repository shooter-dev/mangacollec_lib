from mangacollec.core.exception.exception import MangaCollecException


class UserNotFoundException(MangaCollecException):
    def __init__(self, username: str):
        super().__init__(f"User '{username}' not found")


class UserValidationException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"User validation error: {message}")


class UserAPIException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"User API error: {message}")