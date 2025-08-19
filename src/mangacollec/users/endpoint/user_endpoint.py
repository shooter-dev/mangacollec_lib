from typing import Dict, Any, List

from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.users.interfaces.user_endpoint_interface import IUsersEndpoint


class UserEndpoint(IUsersEndpoint):
    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client

    def get_collection_public(self, username: str) -> Dict[str, Any]:
        return self.client.get(f"/v1/user/{username}/collection")

    def get_collection_private(self) -> Dict[str, Any]:
        return self.client.get("/v1/users/me/collection")

    def get_collection_public_v2(self, username: str) -> Dict[str, Any]:
        return self.client.get(f"/v2/user/{username}/collection")

    def get_collection_private_v2(self) -> Dict[str, Any]:
        if self.client.is_auth:
            return self.client.get("/v2/users/me/collection")
        return {}

    def get_recommendation(self) -> Dict[str, Any]:
        return self.client.get("/v1/users/me/recommendation")

    def get_params_private(self) -> Dict[str, Any]:
        if self.client.is_auth:
            return self.client.get("/v1/users/me")
        return {}

    def get_params_public(self, username: str) -> Dict[str, Any]:
        return self.client.get(f"/v1/users/{username}")

    def follow_editions(self, edition_id: str) -> Dict[str, Any]:
        """
        Suit ou arrête de suivre une édition.
        
        :param edition_id: ID de l'édition à suivre/ne plus suivre
        :param following: True pour suivre, False pour arrêter de suivre
        :return: Réponse de l'API avec les détails du suivi
        """
        if not self.client.is_auth:
            return {}
        
        payload = {
            "edition_id": edition_id,
            "following": True
        }
        
        return self.client.post("/v1/follow_editions/", data=payload)

    def unfollow_editions(self, edition_id: str) -> Dict[str, Any]:
        """
        Arrête de suivre une édition.
        
        :param edition_id: ID de l'édition à ne plus suivre
        :return: Réponse de l'API avec les détails du suivi
        """
        if not self.client.is_auth:
            return {}
        
        return self.client.delete(f"/v1/follow_editions/{edition_id}")

    def read_multiple_volumes(self, ids_volume: List[str]) -> Dict[str, Any]:
        """
        Marque plusieurs volumes comme lus.
        
        :param ids_volume: Liste des IDs des volumes à marquer comme lus
        :return: Réponse de l'API avec les détails des lectures
        """
        if not self.client.is_auth:
            return {}
        
        payload = [{"volume_id": volume_id} for volume_id in ids_volume]
        
        return self.client.post("/v1/reads_multiple/", data=payload)

    def unread_multiple_volumes(self, ids_read: List[str]) -> Dict[str, Any]:
        """
        Marque plusieurs volumes comme non lus (supprime les lectures).
        
        :param ids_read: Liste des IDs de lecture à supprimer
        :return: Réponse de l'API avec les détails des suppressions
        """
        if not self.client.is_auth:
            return {}
        
        payload = [{"id": read_id} for read_id in ids_read]
        
        return self.client.delete("/v1/reads_multiple/", data=payload)