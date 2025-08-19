from pydantic import BaseModel
from typing import List
from mangacollec.kinds.entity.kind import Kind


class KindsEndpointResponse(BaseModel):
    kinds: List[Kind]