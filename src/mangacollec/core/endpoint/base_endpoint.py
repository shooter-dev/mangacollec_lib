from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient
from mangacollec.client.singleton_client import get_mangacollec_client


class BaseEndpoint:
    """
    Classe de base pour tous les endpoints qui gère automatiquement 
    l'injection du client singleton.
    """
    
    def __init__(self, client: IMangaCollecAPIClient = None):
        """
        Initialise l'endpoint avec un client.
        
        :param client: Client API MangaCollec (optionnel, utilise le singleton si non fourni)
        :raises RuntimeError: Si aucun client n'est fourni et que le singleton n'est pas initialisé
        """
        if client is None:
            try:
                client = get_mangacollec_client()
            except RuntimeError as e:
                raise RuntimeError(
                    f"Impossible d'initialiser l'endpoint: {str(e)}\n"
                    "Solution: Initialisez d'abord le client avec get_mangacollec_client(client_id, client_secret) "
                    "ou utilisez MangaCollecEndpointFactory."
                ) from e
        
        self.client = client