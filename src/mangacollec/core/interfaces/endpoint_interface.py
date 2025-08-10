from abc import ABC

from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient


class IEndpoint(ABC):
    """
    Initialise l'accès aux endpoints.

    :param client: Instance du client_anonyme API authentifié
    """

    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client
