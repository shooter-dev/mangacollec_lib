from typing import List
from pydantic import BaseModel
from mangacollec.job.entity.job import Job


class JobsEndpointResponse(BaseModel):
    
    jobs: List[Job]