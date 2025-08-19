from pydantic import BaseModel
from typing import Optional


class Job(BaseModel):
    id: str
    title: str

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.id
