from pydantic import BaseModel


class Type(BaseModel):
    """
    Entité représentant un type de série (Manga, Manhwa, etc.).
    """
    id: str
    title: str
    to_display: bool

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Type(id={self.id}, title={self.title})"