from pydantic import BaseModel
from typing import List


class Serie(BaseModel):
    id: str
    title: str
    type_id: str
    adult_content: bool
    editions_count: int
    tasks_count: int
    kinds_ids: List[str] | None = None

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.id