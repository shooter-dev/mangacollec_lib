from pydantic import BaseModel
from typing import List
from mangacollec.volumes.entity.volume import Volume


class VolumeEndpointResponse(BaseModel):
    volumes: List[Volume]