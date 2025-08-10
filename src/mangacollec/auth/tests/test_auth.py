from unittest.mock import Mock, patch

import pytest
import requests

from mangacollec.auth.auth import AuthMangaCollec


class TestOAuth2Authenticator:
    """Tests for the AuthMangaCollec class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.client_id = "test_client_id"
        self.client_secret = "test_client_secret"
        self.auth = AuthMangaCollec(self.client_id, self.client_secret)

    def test_constructor_success(self):
        """Test successful constructor initialization."""
        assert self.auth.client_id == self.client_id
        assert self.auth.client_secret == self.client_secret

    def test_constructor_with_invalid_credentials(self):
        """Test constructor with invalid credentials."""
        with pytest.raises(ValueError, match="client_id et client_secret sont requis"):
            AuthMangaCollec("", "secret")

        with pytest.raises(ValueError, match="client_id et client_secret sont requis"):
            AuthMangaCollec("client_id", "")

    def test_token_url_constant(self):
        """Test that TOKEN_URL constant is correct."""
        assert AuthMangaCollec.TOKEN_URL == "https://api.mangacollec.com/oauth/token"

    def test_default_headers_structure(self):
        """Test that default headers are properly structured."""
        headers = AuthMangaCollec.DEFAULT_HEADERS
        assert "Accept" in headers
        assert "Accept-language" in headers
        assert "Connection" in headers
        assert "Host" in headers
        assert "User-agent" in headers
        assert headers["Accept"] == "application/json"
        assert headers["Host"] == "api.mangacollec.com"

    @patch('requests.post')
    def test_authenticate_with_password_success(self, mock_post):
        """Test successful password authentication."""
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "refresh_token": "test_refresh_token",
            "token_type": "Bearer",
            "expires_in": 3600,
            "created_at": 1234567890
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        username = "test@example.com"
        password = "test_password"

        result = self.auth.authenticate_with_password(username, password)

        # Verify the request was made correctly
        mock_post.assert_called_once_with(
            AuthMangaCollec.TOKEN_URL,
            headers=AuthMangaCollec.DEFAULT_HEADERS,
            data={
                "grant_type": "password",
                "username": username,
                "password": password,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
        )

        # Verify the response - result is now a TokenResponce object
        assert result.access_token == "test_access_token"
        assert result.refresh_token == "test_refresh_token"

    def test_authenticate_with_password_invalid_params(self):
        """Test password authentication with invalid parameters."""
        with pytest.raises(ValueError, match="username et password sont requis pour se connecter"):
            self.auth.authenticate_with_password("", "password")

        with pytest.raises(ValueError, match="username et password sont requis pour se connecter"):
            self.auth.authenticate_with_password("username", "")

        with pytest.raises(ValueError, match="username et password sont requis pour se connecter"):
            self.auth.authenticate_with_password("", "password")

    @patch('requests.post')
    def test_authenticate_with_password_401_error(self, mock_post):
        """Test password authentication with 401 error."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_post.return_value = mock_response
        mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)

        with pytest.raises(ConnectionError, match="Identifiants invalides"):
            self.auth.authenticate_with_password("test@example.com", "wrong_password")

    @patch('requests.post')
    def test_authenticate_with_password_other_http_error(self, mock_post):
        """Test password authentication with other HTTP error."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Server Error", response=mock_response)

        with pytest.raises(ConnectionError, match="Erreur d'authentification"):
            self.auth.authenticate_with_password("test@example.com", "password")

    @patch('requests.post')
    def test_authenticate_with_password_connection_error(self, mock_post):
        """Test password authentication with connection error."""
        mock_post.side_effect = requests.exceptions.ConnectionError("Network error")

        with pytest.raises(ConnectionError, match="Erreur de connexion"):
            self.auth.authenticate_with_password("test@example.com", "password")

    @patch('requests.post')
    def test_authenticate_with_client_credentials_success(self, mock_post):
        """Test successful client credentials authentication."""
        # Mock successful response
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "expires_in": 3600,
            "created_at": 1234567890
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = self.auth.authenticate_with_client_credentials()

        # Verify the request was made correctly
        mock_post.assert_called_once_with(
            AuthMangaCollec.TOKEN_URL,
            headers=AuthMangaCollec.DEFAULT_HEADERS,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
        )

        # Verify the response - result is now a TokenResponce object
        assert result.access_token == "test_access_token"
        assert result.token_type == "Bearer"

    @patch('requests.post')
    def test_authenticate_with_client_credentials_401_error(self, mock_post):
        """Test client credentials authentication with 401 error."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_post.return_value = mock_response
        mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)

        with pytest.raises(ConnectionError, match="Identifiants client_anonyme invalides"):
            self.auth.authenticate_with_client_credentials()

    @patch('requests.post')
    def test_authenticate_with_client_credentials_other_http_error(self, mock_post):
        """Test client credentials authentication with other HTTP error."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Server Error", response=mock_response)

        with pytest.raises(ConnectionError, match="Erreur d'authentification"):
            self.auth.authenticate_with_client_credentials()

    @patch('requests.post')
    def test_authenticate_with_client_credentials_connection_error(self, mock_post):
        """Test client credentials authentication with connection error."""
        mock_post.side_effect = requests.exceptions.RequestException("Network error")

        with pytest.raises(ConnectionError, match="Erreur de connexion"):
            self.auth.authenticate_with_client_credentials()
