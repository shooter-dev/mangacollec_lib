from pydantic import BaseModel


class Genre(BaseModel):
    id: str
    title: str
    to_display: bool

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.id