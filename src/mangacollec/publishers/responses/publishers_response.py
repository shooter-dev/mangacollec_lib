from pydantic import BaseModel
from typing import List
from mangacollec.publishers.entity.publisher import Publisher


class PublishersEndpointResponse(BaseModel):
    publishers: List[Publisher]