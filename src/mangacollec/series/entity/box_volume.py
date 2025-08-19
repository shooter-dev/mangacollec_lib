from pydantic import BaseModel


class BoxVolume(BaseModel):
    """
    Entité représentant la relation entre un coffret et un volume.
    """
    id: str
    box_id: str
    volume_id: str
    included: bool

    def __repr__(self):
        return f"BoxVolume(id={self.id}, box_id={self.box_id}, volume_id={self.volume_id})"