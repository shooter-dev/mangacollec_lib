from pydantic import BaseModel
from typing import Optional


class Box(BaseModel):
    """
    Entité représentant un coffret.
    """
    id: str
    title: Optional[str]
    number: int
    release_date: Optional[str] = None
    isbn: Optional[str] = None
    asin: Optional[str] = None
    commercial_stop: Optional[bool] = None
    box_edition_id: str
    box_possessions_count: Optional[int] = None
    image_url: Optional[str] = None

    def __str__(self):
        return self.title or f"Coffret #{self.number}"

    def __repr__(self):
        return f"Box(id={self.id}, title={self.title})"