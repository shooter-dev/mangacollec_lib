import time

import requests
from requests import Response

from mangacollec.auth import AuthMangaCollec, IAuthMangaCollec
from mangacollec.auth.responce.token_responce import TokenResponce
from mangacollec.client.interfaces.client_interface import IMangaCollecAPIClient


class MangaCollecAPIClient(IMangaCollecAPIClient):
    """Client pour interagir avec l'API MangaCollec via OAuth2.
    Prend en charge l'authentification avec client_id/client_secret
    ou username/password."""

    # Constante pour éviter les magic numbers
    TOKEN_EXPIRY_BUFFER_SECONDS = 60


    def _authenticate(self) -> None:
        """Authentifie le client_anonyme selon les identifiants fournis
        et initialise le token."""
        auth: IAuthMangaCollec = AuthMangaCollec(self.client_id, self.client_secret)

        # Vérifie si les credentials utilisateur sont disponibles.
        if self._has_user_credentials(): # fair un client password
            token_response: TokenResponce = auth.authenticate_with_password(self.email, self.password)
            self.is_auth = bool(token_response.access_token)
        else: # alor création d'un client anonyme
            token_response: TokenResponce = auth.authenticate_with_client_credentials()
            self.is_auth = False

        # Met à jour les propriétés de token depuis la réponse du module auth
        self._update_token_from_token_response(token_response)


    def _has_user_credentials(self) -> bool:
        """Vérifie si les credentials utilisateur sont disponibles."""
        return bool(self.email and self.password)


    def _update_token_from_token_response(self, token_response: TokenResponce) -> None:
        """Met à jour les propriétés de token depuis la réponse du module auth."""
        self.access_token = token_response.access_token
        self.token_type = token_response.token_type
        self.token_expiry = token_response.created_at + token_response.expires_in
        self.refresh_token = token_response.refresh_token


    def _refresh_access_token(self) -> None:
        """Rafraîchit le token d'accès à l'aide du refresh_token.
        Fonctionne uniquement si grant_type=password a été utilisé."""
        if not self.refresh_token:
            raise RuntimeError(
                "Aucun refresh_token disponible pour rafraîchir le token."
            )

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        response = requests.post(self.TOKEN_URL, data=payload)
        response.raise_for_status()

        data = response.json()

        self.access_token = data["access_token"]
        self.token_type = data["token_type"]
        self.token_expiry = data["created_at"] + data["expires_in"]
        self.refresh_token = data.get("refresh_token")


    def _ensure_token_valid(self) -> None:
        """Vérifie la validité du token. Le rafraîchit si expiré et possible."""
        if self._is_token_still_valid():
            return

        self._handle_expired_token()


    def _is_token_still_valid(self) -> bool:
        """Vérifie si le token est encore valide avec un buffer de sécurité."""
        if not self.token_expiry:
            return False

        return time.time() < self.token_expiry - self.TOKEN_EXPIRY_BUFFER_SECONDS


    def _handle_expired_token(self) -> None:
        """Gère le renouvellement du token expiré."""
        if self.refresh_token:
            self._refresh_access_token()
        else:
            self._authenticate()


    def _call_request(self, method: str, endpoint: str, **kwargs) -> Response:
        """
        Effectue une requête HTTP authentifiée credentials/password.
        """
        self._ensure_token_valid()

        headers = kwargs.pop("headers", {})

        headers["Authorization"] = f"{self.token_type} {self.access_token}"

        url = f"{self.BASE_URL}{endpoint}"

        response = requests.request(
            method=method, url=url, headers=headers, proxies=None, **kwargs
        )

        response.raise_for_status()

        return response.json()


    def get(self, endpoint: str, params: dict | None = None) -> Response:
        """
        Effectue une requête GET vers l'API.
        """
        return self._call_request("GET", endpoint, params=params)


    def post(self, endpoint: str, data: dict | None = None) -> Response:
        """
        Effectue une requête POST vers l'API.
        """
        return self._call_request("POST", endpoint, json=data)


    def delete(self, endpoint: str) -> Response:
        """
        Effectue une requête DELETE vers l'API.
        """
        return self._call_request("DELETE", endpoint)

    def __repr__(self) -> str:
        """
        Représentation string du client_anonyme avec informations de statut.
        """
        auth_type = "password" if self._has_user_credentials() else "client_credentials"
        token_status = "valid" if self._is_token_still_valid() else "expired/invalid"

        return (
            f"MangaCollecAPIClient("
            f"auth_type='{auth_type}', "
            f"is_auth={self.is_auth}, "
            f"token_status='{token_status}', "
            f"username='{self.username or 'N/A'}', "
            f"is_premium={self.is_premium}"
            f")"
        )

    def __str__(self) -> str:
        """
        Représentation string user-friendly du client_anonyme.
        """
        auth_mode = "Utilisateur connecté" if self.is_auth else "Client anonyme"
        premium_status = " (Premium)" if self.is_premium else ""
        user_info = f" - {self.username}" if self.username else ""

        return f"MangaCollec API Client: {auth_mode}{premium_status}{user_info}"
