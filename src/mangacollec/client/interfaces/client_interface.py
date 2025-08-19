from abc import ABC, abstractmethod


class IMangaCollecAPIClient(ABC):
    """
    Client pour interagir avec l'API MangaCollec via OAuth2.
    Prend en charge l'authentification avec client_id/client_secret ou username/password.
    """

    TOKEN_URL: str = "https://api.mangacollec.com/oauth/token/"
    BASE_URL: str = "https://api.mangacollec.com/"

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        email: str | None = None,
        password: str | None = None,
        proxy: dict | None = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.email = email
        self.password = password

        self.access_token: str | None = None
        self.refresh_token: str | None = None
        self.token_type: str | None = None
        self.token_expiry: int | None = None

        self.proxy: dict | None = proxy

        self.is_auth: bool = False
        self.is_premium: bool = False

        self.username: str = ""

        self._authenticate()

    @abstractmethod
    def _authenticate(self) -> None:
        """
        Authentifie le client_anonyme selon les identifiants fournis et initialise le token.
        """
        pass

    @abstractmethod
    def _refresh_access_token(self) -> None:
        """
        Rafraîchit le token d'accès à l'aide du refresh_token.
        Fonctionne uniquement si grant_type=password a été utilisé.
        """
        pass

    @abstractmethod
    def _ensure_token_valid(self):
        """
        Vérifie la validité du token. Le rafraîchit si expiré et possible.
        """
        pass

    @abstractmethod
    def _call_request(self, method: str, endpoint: str, **kwargs):
        """
        Effectue une requête HTTP authentifiée.
        """
        pass

    @abstractmethod
    def get(
        self, endpoint: str, params: dict | None = None
    ) -> dict | list | None:
        """
        Effectue une requête GET vers l'API.
        """
        pass

    @abstractmethod
    def post(self, endpoint: str, data: dict | None = None) -> dict | list | None:
        """
        Effectue une requête POST vers l'API.
        """
        pass

    @abstractmethod
    def delete(self, endpoint: str, data: dict | None = None) -> dict | list | None:
        """
        Effectue une requête DELETE vers l'API.
        """
        pass
