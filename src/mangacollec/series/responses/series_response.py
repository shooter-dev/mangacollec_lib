from pydantic import BaseModel
from typing import List
from mangacollec.series.entity.serie import Serie


class SeriesEndpointResponse(BaseModel):
    series: List[Serie]