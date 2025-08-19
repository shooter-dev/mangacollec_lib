from abc import ABC, abstractmethod

from mangacollec.auth.response.token_response import TokenResponse


class IAuthMangaCollec(ABC):
    """
    Classe responsable de l'authentification OAuth2 auprès de l'API MangaCollec.

    Elle supporte deux modes :
    - grant_type=password (avec email/mot de passe)
    - grant_type=client_credentials (avec client_id/client_secret)
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Initialise l'authenticator avec les identifiants client_anonyme.

        :param client_id: ID client_anonyme fourni par MangaCollec
        :param client_secret: Secret client_anonyme fourni par MangaCollec
        :raises ValueError: Si les identifiants sont invalides
        """
        if not client_id or not client_secret:
            raise ValueError("client_id et client_secret sont requis")

        self.client_id = client_id
        self.client_secret = client_secret

    @abstractmethod
    def authenticate_with_password(self, username: str, password: str) -> TokenResponse:
        """
        Authentifie l'utilisateur avec email/mot de passe (grant_type=password).

        :param username: Email de l'utilisateur
        :param password: Mot de passe
        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ValueError: Si les paramètres sont invalides
        :raises ConnectionError: Si l'authentification échoue
        """

    @abstractmethod
    def authenticate_with_client_credentials(self) -> TokenResponse:
        """
        Authentifie via client_id/client_secret uniquement (grant_type=client_credentials).

        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ConnectionError: Si l'authentification échoue
        """
