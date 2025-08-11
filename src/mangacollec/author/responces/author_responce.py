from typing import List, TYPE_CHECKING, Any

from pydantic import BaseModel

from mangacollec.author.entity.author import Author


class AuthorEndpointResponce(BaseModel):

    authors: List[Author]

    tasks: List[Any] = []

    jobs: List[Any] = []

    series: List[Any] = []

    editions: List[Any] = []

    volumes: List[Any] = []
