from pydantic import BaseModel


class TokenResponce(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    created_at: int