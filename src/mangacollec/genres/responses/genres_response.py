from pydantic import BaseModel
from typing import List
from mangacollec.genres.entity.genre import Genre


class GenresEndpointResponse(BaseModel):
    genres: List[Genre]