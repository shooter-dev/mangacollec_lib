from typing import List, TYPE_CHECKING, Any

from pydantic import BaseModel

from mangacollec.author.entity.author import Author
from mangacollec.editions.entity.edition import Edition
from mangacollec.job import Job
from mangacollec.series.entity.serie import Serie
from mangacollec.volumes.entity.volume import Volume


class AuthorEndpointResponse(BaseModel):

    authors: List[Author]

    tasks: List[Any] = []

    jobs: List[Job] = []

    series: List[Serie] = []

    editions: List[Edition] = []

    volumes: List[Volume] = []
