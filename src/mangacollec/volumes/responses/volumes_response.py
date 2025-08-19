from pydantic import BaseModel
from typing import List
from mangacollec.volumes.entity.volume import Volume


class VolumesEndpointResponse(BaseModel):
    volumes: List[Volume]