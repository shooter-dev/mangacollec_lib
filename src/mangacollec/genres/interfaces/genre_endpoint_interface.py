from abc import ABC, abstractmethod
from typing import Dict, Any
from mangacollec.genres.responses.genres_response import GenresEndpointResponse


class IGenresEndpoint(ABC):
    @abstractmethod
    def get_all_genres(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_all_genres_v2(self) -> GenresEndpointResponse:
        pass