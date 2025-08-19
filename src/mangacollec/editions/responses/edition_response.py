from pydantic import BaseModel
from typing import List
from mangacollec.editions.entity.edition import Edition


class EditionEndpointResponse(BaseModel):
    editions: List[Edition]