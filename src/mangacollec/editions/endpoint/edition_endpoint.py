from typing import Dict, Any, List

from mangacollec.editions.converter.edition_converter import EditionConverter
from mangacollec.editions.responses.edition_response import EditionEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.editions.interfaces.edition_endpoint_interface import IEditionsEndpoint
from mangacollec.editions.entity.edition import Edition


class EditionEndpoint(IEditionsEndpoint):
    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client

    def get_edition_by_id(self, edition_id: str) -> Dict[str, Any]:
        return self.client.get(f"/v1/editions/{edition_id}")

    def get_edition_by_id_v2(self, edition_id: str) -> EditionEndpointResponse:
        result_endpoint = self.client.get(f"/v2/editions/{edition_id}")

        converter = EditionConverter()
        editions = []
        
        if 'editions' in result_endpoint:
            for item_edition in result_endpoint['editions']:
                editions.append(converter.deserialize(item_edition))
        
        return EditionEndpointResponse(editions=editions)