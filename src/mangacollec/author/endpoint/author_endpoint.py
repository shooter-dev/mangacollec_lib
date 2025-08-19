from typing import Dict, Any, List

from mangacollec.author.converter.author_converter import AuthorConverter
from mangacollec.author.responses.author_response import AuthorEndpointResponse
from mangacollec.author.responses.authors_response import AuthorsEndpointResponse
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.author.interfaces.author_endpoint_interface import IAuthorsEndpoint
from mangacollec.author.entity.author import Author



class AuthorEndpoint(IAuthorsEndpoint):
    """
    Implémentation des opérations pour les auteurs dans l'API MangaCollec.
    """
    
    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise endpoint des auteurs.

        :param client: Client API MangaCollec
        """
        self.client = client

    def get_all(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des auteurs disponibles sur MangaCollec.

        :return: Liste des auteurs
        """
        return self.client.get("/v1/authors")

    def get_by_id(self, author_id: str) -> Dict[str, Any]:
        """
        Récupère un auteur spécifique à partir de son ID.

        :param author_id: Identifiant de l'auteur
        :return: Détails de l'auteur
        """
        return self.client.get(f"/v1/authors/{author_id}")

    def get_all_v2(self) -> AuthorsEndpointResponse:
        """
        Récupère la liste complète des auteurs disponibles sur MangaCollec (API v2).

        :return: AuthorsEndpointResponse
        """
        result_endpoint = self.client.get("/v2/authors")

        authors: List[Author] = []

        converter = AuthorConverter()

        for item_author in result_endpoint['authors']:
            authors.append(converter.deserialize(item_author))

        return AuthorsEndpointResponse(authors=authors)

    def get_by_id_v2(self, author_id: str) -> AuthorEndpointResponse:
        """
        Récupère un auteur spécifique à partir de son ID (API v2).

        :param author_id: Identifiant de l'auteur
        :return: Détails de l'auteur
        """
        result_endpoint = self.client.get(f"/v2/authors/{author_id}")

        converter = AuthorConverter()
        authors = []
        
        if 'authors' in result_endpoint:
            for item_author in result_endpoint['authors']:
                authors.append(converter.deserialize(item_author))
        
        return AuthorEndpointResponse(authors=authors)
