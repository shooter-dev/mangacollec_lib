from pydantic import BaseModel


class Kind(BaseModel):
    id: str
    title: str

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.id