from abc import ABC, abstractmethod
from typing import Dict, Any
from mangacollec.kinds.responses.kinds_response import KindsEndpointResponse


class IKindsEndpoint(ABC):
    @abstractmethod
    def get_all_kinds(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_all_kinds_v2(self) -> KindsEndpointResponse:
        pass