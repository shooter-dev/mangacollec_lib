from pydantic import BaseModel
from typing import List, Dict, Any


class User(BaseModel):
    username: str
    collection: List[Dict[str, Any]] | None = None

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username