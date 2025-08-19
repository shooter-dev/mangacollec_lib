from typing import Dict, List

from pydantic import BaseModel

from mangacollec.author.entity.author import Author


class AuthorsEndpointResponse(BaseModel):

    authors: List[Author] = []