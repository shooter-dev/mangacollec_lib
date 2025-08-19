from pydantic import BaseModel
from typing import List
from mangacollec.users.entity.user import User


class UserEndpointResponse(BaseModel):
    users: List[User]