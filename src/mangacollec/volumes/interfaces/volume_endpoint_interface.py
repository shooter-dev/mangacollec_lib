from abc import ABC, abstractmethod
from typing import Dict, Any
from mangacollec.volumes.responses.volume_response import VolumeEndpointResponse
from mangacollec.volumes.responses.volumes_response import VolumesEndpointResponse


class IVolumesEndpoint(ABC):
    @abstractmethod
    def get_volume_by_id(self, volume_id: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_volumes_news(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_volume_by_id_v2(self, volume_id: str) -> VolumeEndpointResponse:
        pass

    @abstractmethod
    def get_volumes_news_v2(self) -> VolumesEndpointResponse:
        pass