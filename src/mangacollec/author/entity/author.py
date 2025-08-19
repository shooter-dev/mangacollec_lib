from pydantic import BaseModel
from typing import List, Optional


class Author(BaseModel):
    id: str
    name: str
    first_name: str | None
    tasks_count: Optional[int] = None

    def __str__(self):
        if self.first_name is None:
            return self.name

        return self.name + " " + self.first_name

    def __repr__(self):
        return self.id
