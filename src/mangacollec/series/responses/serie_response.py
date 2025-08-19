from pydantic import BaseModel
from typing import List
from mangacollec.series.entity.serie import Serie
from mangacollec.series.entity.type import Type
from mangacollec.series.entity.task import Task
from mangacollec.series.entity.box_edition import BoxEdition
from mangacollec.series.entity.box import Box
from mangacollec.series.entity.box_volume import BoxVolume
from mangacollec.kinds.entity.kind import Kind
from mangacollec.job.entity.job import Job
from mangacollec.author.entity.author import Author
from mangacollec.editions.entity.edition import Edition
from mangacollec.publishers.entity.publisher import Publisher
from mangacollec.volumes.entity.volume import Volume


class SerieEndpointResponse(BaseModel):
    series: List[Serie]
    types: List[Type]
    kinds: List[Kind]
    tasks: List[Task]
    jobs: List[Job]
    authors: List[Author]
    editions: List[Edition]
    publishers: List[Publisher]
    volumes: List[Volume]
    box_editions: List[BoxEdition]
    boxes: List[Box]
    box_volumes: List[BoxVolume]