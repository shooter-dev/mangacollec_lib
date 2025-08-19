from typing import Dict, Any, List

from mangacollec.publishers.converter.publisher_converter import PublisherConverter
from mangacollec.publishers.responses.publisher_response import PublisherEndpointResponse
from mangacollec.publishers.responses.publishers_response import PublishersEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.publishers.interfaces.publisher_endpoint_interface import IPublishersEndpoint
from mangacollec.publishers.entity.publisher import Publisher


class PublisherEndpoint(IPublishersEndpoint):
    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client

    def get_all_publishers(self) -> Dict[str, Any]:
        return self.client.get("/v1/publishers")

    def get_publisher_by_id(self, publisher_id: str) -> Dict[str, Any]:
        return self.client.get(f"/v1/publishers/{publisher_id}")

    def get_all_publishers_v2(self) -> PublishersEndpointResponse:
        result_endpoint = self.client.get("/v2/publishers")
        
        publishers: List[Publisher] = []
        converter = PublisherConverter()

        for item_publisher in result_endpoint['publishers']:
            publishers.append(converter.deserialize(item_publisher))

        return PublishersEndpointResponse(publishers=publishers)

    def get_publisher_by_id_v2(self, publisher_id: str) -> PublisherEndpointResponse:
        result_endpoint = self.client.get(f"/v2/publishers/{publisher_id}")

        converter = PublisherConverter()
        publishers = []
        
        if 'publishers' in result_endpoint:
            for item_publisher in result_endpoint['publishers']:
                publishers.append(converter.deserialize(item_publisher))
        
        return PublisherEndpointResponse(publishers=publishers)