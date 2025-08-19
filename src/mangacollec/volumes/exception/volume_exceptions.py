from mangacollec.core.exception.exception import MangaCollecException


class VolumeNotFoundException(MangaCollecException):
    def __init__(self, volume_id: str):
        super().__init__(f"Volume with ID '{volume_id}' not found")


class VolumeValidationException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Volume validation error: {message}")


class VolumeAPIException(MangaCollecException):
    def __init__(self, message: str):
        super().__init__(f"Volume API error: {message}")