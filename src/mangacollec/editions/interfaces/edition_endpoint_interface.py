from abc import ABC, abstractmethod
from typing import Dict, Any
from mangacollec.editions.responses.edition_response import EditionEndpointResponse


class IEditionsEndpoint(ABC):
    @abstractmethod
    def get_edition_by_id(self, edition_id: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_edition_by_id_v2(self, edition_id: str) -> EditionEndpointResponse:
        pass