from typing import Dict, Any, List

from mangacollec.volumes.converter.volume_converter import VolumeConverter
from mangacollec.volumes.responses.volume_response import VolumeEndpointResponse
from mangacollec.volumes.responses.volumes_response import VolumesEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.volumes.interfaces.volume_endpoint_interface import IVolumesEndpoint
from mangacollec.volumes.entity.volume import Volume


class VolumeEndpoint(IVolumesEndpoint):
    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client

    def get_volume_by_id(self, volume_id: str) -> Dict[str, Any]:
        return self.client.get(f"/v1/volumes/{volume_id}")

    def get_volumes_news(self) -> Dict[str, Any]:
        return self.client.get("/v1/volumes/news")

    def get_volume_by_id_v2(self, volume_id: str) -> VolumeEndpointResponse:
        result_endpoint = self.client.get(f"/v2/volumes/{volume_id}")

        converter = VolumeConverter()
        volumes = []
        
        if 'volumes' in result_endpoint:
            for item_volume in result_endpoint['volumes']:
                volumes.append(converter.deserialize(item_volume))
        
        return VolumeEndpointResponse(volumes=volumes)

    def get_volumes_news_v2(self) -> VolumesEndpointResponse:
        result_endpoint = self.client.get("/v2/volumes/news")
        
        volumes: List[Volume] = []
        converter = VolumeConverter()

        for item_volume in result_endpoint['volumes']:
            volumes.append(converter.deserialize(item_volume))

        return VolumesEndpointResponse(volumes=volumes)