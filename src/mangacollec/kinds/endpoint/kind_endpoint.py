from typing import Dict, Any, List

from mangacollec.kinds.converter.kind_converter import KindConverter
from mangacollec.kinds.responses.kinds_response import KindsEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.kinds.interfaces.kind_endpoint_interface import IKindsEndpoint
from mangacollec.kinds.entity.kind import Kind


class KindEndpoint(IKindsEndpoint):
    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client

    def get_all_kinds(self) -> Dict[str, Any]:
        return self.client.get("/v1/kinds")

    def get_all_kinds_v2(self) -> KindsEndpointResponse:
        result_endpoint = self.client.get("/v2/kinds")
        
        kinds: List[Kind] = []
        converter = KindConverter()

        for item_kind in result_endpoint['kinds']:
            kinds.append(converter.deserialize(item_kind))

        return KindsEndpointResponse(kinds=kinds)