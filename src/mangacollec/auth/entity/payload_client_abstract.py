from abc import ABC, abstractmethod
from pydantic import BaseModel


class PayloadClientAbstract(BaseModel, ABC):
    grant_type: str
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass