from abc import ABC, abstractmethod
from typing import Dict, Any, List
from mangacollec.users.responses.user_response import UserEndpointResponse


class IUsersEndpoint(ABC):
    @abstractmethod
    def get_collection_public(self, username: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_collection_private(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_collection_public_v2(self, username: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_collection_private_v2(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_recommendation(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_params_private(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_params_public(self, username: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def follow_editions(self, username: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def unfollow_editions(self, username: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def read_multiple_volumes(self, ids_volume: List[str]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def unread_multiple_volumes(self, ids_volume: List[str]) -> Dict[str, Any]:
        pass