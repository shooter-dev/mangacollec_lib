from pydantic import BaseModel


class BoxEdition(BaseModel):
    """
    Entité représentant une édition de coffrets.
    """
    id: str
    title: str
    publisher_id: str
    boxes_count: int
    adult_content: bool
    box_follow_editions_count: int

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"BoxEdition(id={self.id}, title={self.title})"