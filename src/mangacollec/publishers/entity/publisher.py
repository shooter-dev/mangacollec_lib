from pydantic import BaseModel
from typing import Optional


class Publisher(BaseModel):
    id: str
    title: str
    closed: Optional[bool] = None
    editions_count: Optional[int] = None
    no_amazon: Optional[bool] = None

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.id