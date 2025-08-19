from abc import ABC, abstractmethod
from typing import Dict, Any
from mangacollec.publishers.responses.publisher_response import PublisherEndpointResponse
from mangacollec.publishers.responses.publishers_response import PublishersEndpointResponse


class IPublishersEndpoint(ABC):
    @abstractmethod
    def get_all_publishers(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_publisher_by_id(self, publisher_id: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_all_publishers_v2(self) -> PublishersEndpointResponse:
        pass

    @abstractmethod
    def get_publisher_by_id_v2(self, publisher_id: str) -> PublisherEndpointResponse:
        pass