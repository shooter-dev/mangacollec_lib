from pydantic import BaseModel
from datetime import date


class Volume(BaseModel):
    id: str
    title: str | None
    number: int
    release_date: str | None
    isbn: str | None
    asin: str | None
    edition_id: str
    possessions_count: int
    not_sold: bool
    image_url: str | None
    nb_pages: int | None
    content: str | None

    def __str__(self):
        if self.title:
            return f"Volume {self.number}: {self.title}"
        return f"Volume {self.number}"

    def __repr__(self):
        return self.id