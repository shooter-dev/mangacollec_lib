import requests

from mangacollec.auth.interfaces.auth_interface import IAuthMangaCollec
from mangacollec.auth.entity.payload_client_abstract import PayloadClientAbstract
from mangacollec.auth.entity.payload_client_credential import PayloadClientCredential
from mangacollec.auth.entity.payload_client_password import PayloadClientPassword
from mangacollec.auth.response.token_response import TokenResponse


class AuthMangaCollec(IAuthMangaCollec):
    """
    Classe responsable de l'authentification OAuth2 auprès de l'API MangaCollec.

    Elle supporte deux modes :
    - grant_type=password (avec email/mot de passe)
    - grant_type=client_credentials (avec client_id/client_secret)
    """

    TOKEN_URL = "https://api.mangacollec.com/oauth/token"
    HTTP_UNAUTHORIZED = 401
    DEFAULT_HEADERS = {
        "Accept": "application/json",
        "Accept-language": "fr-FR,fr;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "api.mangacollec.com",
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }

    def authenticate_with_password(self, username: str, password: str) -> TokenResponse:
        """
        Authentifie l'utilisateur avec email/mot de passe (grant_type=password).

        :param username: Email de l'utilisateur
        :param password: Mot de passe
        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ValueError: Si les paramètres sont invalides
        :raises ConnectionError: Si l'authentification échoue
        """
        self._validate_password_params(username, password)

        payload: PayloadClientPassword = self._build_password_payload(username, password)
        return self._execute_auth_request(payload, "Identifiants invalides")


    def authenticate_with_client_credentials(self) -> TokenResponse:
        """
        Authentifie via client_id/client_secret uniquement (grant_type=client_credentials).

        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ConnectionError: Si l'authentification échoue
        """
        payload: PayloadClientCredential = self._build_client_credentials_payload()
        return self._execute_auth_request(payload, "Identifiants client_anonyme invalides")


    def _validate_password_params(self, username: str, password: str) -> None:
        """Valide les paramètres username et password."""
        if not username or not password:
            raise ValueError("username et password sont requis pour se connecter")

    def _build_password_payload(self, username: str, password: str) -> PayloadClientPassword:
        """Construit le payload pour l'authentification par mot de passe."""
        return PayloadClientPassword(
            username=username,
            password=password,
            client_id=self.client_id,
            client_secret=self.client_secret
        )


    def _build_client_credentials_payload(self) -> PayloadClientCredential:
        """Construit le payload pour l'authentification par client_anonyme credentials."""
        return PayloadClientCredential(
            client_id=self.client_id,
            client_secret=self.client_secret
        )


    def _execute_auth_request(self, payload: PayloadClientAbstract, error_401_msg: str) -> TokenResponse:
        """Exécute la requête d'authentification et gère les erreurs."""
        try:
            response = requests.post(
                self.TOKEN_URL, headers=self.DEFAULT_HEADERS, data=payload.to_dict()
            )

            response.raise_for_status()

            response_data = response.json()
            
            return TokenResponse(
                access_token=response_data["access_token"],
                token_type=response_data["token_type"],
                expires_in=response_data["expires_in"],
                refresh_token=response_data.get("refresh_token", ""),
                created_at=response_data["created_at"]
            )
        except requests.exceptions.HTTPError as e:
            self._handle_http_error(e, error_401_msg)
            raise  # Cette ligne ne sera jamais atteinte car _handle_http_error lève toujours une exception
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Erreur de connexion: {str(e)}") from e

    def _handle_http_error(self, error: requests.exceptions.HTTPError, error_401_msg: str) -> None:
        """Gère les erreurs HTTP spécifiques."""
        if hasattr(error, 'response') and error.response and error.response.status_code == self.HTTP_UNAUTHORIZED:
            raise ConnectionError(error_401_msg) from error

        raise ConnectionError(f"Erreur d'authentification: {str(error)}") from error
