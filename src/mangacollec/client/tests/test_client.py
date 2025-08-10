import time
from unittest.mock import Mock, patch

import pytest
import requests

from mangacollec.client import MangaCollecAPIClient


class TestMangaCollecAPIClient:

    def setup_method(self):
        self.client_id = "test_client_id"
        self.client_secret = "test_client_secret"
        self.email = "test@example.com"
        self.password = "test_password"

    @patch('requests.post')
    def test_authenticate_with_client_credentials(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        MangaCollecAPIClient(self.client_id, self.client_secret)

        
        assert mock_post.called
        call_args = mock_post.call_args

        
        payload = call_args[1]['data']
        assert payload["grant_type"] == "client_credentials"
        assert payload["client_id"] == self.client_id
        assert payload["client_secret"] == self.client_secret
        assert "username" not in payload
        assert "password" not in payload

    @patch('requests.post')
    def test_authenticate_with_password(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600,
            "refresh_token": "test_refresh_token"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        MangaCollecAPIClient(
            self.client_id,
            self.client_secret,
            email=self.email,
            password=self.password
        )

        
        assert mock_post.called
        call_args = mock_post.call_args

        
        payload = call_args[1]['data']
        assert payload["grant_type"] == "password"
        assert payload["client_id"] == self.client_id
        assert payload["client_secret"] == self.client_secret
        assert payload["username"] == self.email
        assert payload["password"] == self.password

    @patch('requests.post')
    def test_authenticate_sets_token_properties(self, mock_post):
        created_at = int(time.time())
        expires_in = 3600

        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": created_at,
            "expires_in": expires_in,
            "refresh_token": "test_refresh_token"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(
            self.client_id,
            self.client_secret,
            email=self.email,
            password=self.password
        )

        assert client.access_token == "test_access_token"
        assert client.token_type == "Bearer"
        assert client.token_expiry == created_at + expires_in
        assert client.refresh_token == "test_refresh_token"
        assert client.is_auth is True

    @patch('requests.post')
    def test_authenticate_client_credentials_sets_is_auth_false(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        assert client.is_auth is False

    @patch('requests.post')
    def test_refresh_access_token_success(self, mock_post):
        
        initial_response = Mock()
        initial_response.json.return_value = {
            "access_token": "initial_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600,
            "refresh_token": "refresh_token"
        }
        initial_response.raise_for_status.return_value = None

        
        refresh_response = Mock()
        refresh_response.json.return_value = {
            "access_token": "new_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600,
            "refresh_token": "new_refresh_token"
        }
        refresh_response.raise_for_status.return_value = None

        mock_post.side_effect = [initial_response, refresh_response]

        client = MangaCollecAPIClient(
            self.client_id,
            self.client_secret,
            email=self.email,
            password=self.password
        )

        
        client._refresh_access_token()

        
        assert mock_post.call_count == 2
        refresh_call = mock_post.call_args_list[1]

        
        refresh_payload = refresh_call[1]['data']
        assert refresh_payload['grant_type'] == "refresh_token"
        assert refresh_payload['refresh_token'] == "refresh_token"
        assert refresh_payload['client_id'] == self.client_id
        assert refresh_payload['client_secret'] == self.client_secret

        
        assert client.access_token == "new_access_token"
        assert client.refresh_token == "new_refresh_token"

    @patch('requests.post')
    def test_refresh_access_token_no_refresh_token(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)
        client.refresh_token = None

        with pytest.raises(RuntimeError, match="Aucun refresh_token disponible"):
            client._refresh_access_token()

    @patch('requests.post')
    def test_ensure_token_valid_not_expired(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        
        client.token_expiry = int(time.time()) + 3600

        with patch.object(client, '_refresh_access_token') as mock_refresh:
            client._ensure_token_valid()
            
            mock_refresh.assert_not_called()

    @patch('requests.post')
    def test_ensure_token_valid_expired_with_refresh_token(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600,
            "refresh_token": "refresh_token"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(
            self.client_id,
            self.client_secret,
            email=self.email,
            password=self.password
        )

        
        client.token_expiry = int(time.time()) - 100

        with patch.object(client, '_refresh_access_token') as mock_refresh:
            client._ensure_token_valid()
            
            mock_refresh.assert_called_once()

    @patch('requests.post')
    def test_ensure_token_valid_expired_no_refresh_token(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        
        client.token_expiry = int(time.time()) - 100
        client.refresh_token = None

        with patch.object(client, '_authenticate') as mock_authenticate:
            client._ensure_token_valid()
            
            mock_authenticate.assert_called_once()

    @staticmethod
    def _setup_auth_mock(mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

    @staticmethod
    def _setup_request_mock(mock_request):
        mock_request_response = Mock()
        mock_request_response.json.return_value = {"status": "success"}
        mock_request_response.raise_for_status.return_value = None
        mock_request.return_value = mock_request_response

    @staticmethod
    def _extract_call_args(call_args):
        if call_args[0] and len(call_args[0]) >= 2:
            return call_args[0][0], call_args[0][1]
        return call_args[1]['method'], call_args[1]['url']

    @patch('requests.post')
    def test_call_request_success(self, mock_post):
        TestMangaCollecAPIClient._setup_auth_mock(mock_post)
        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        with patch('requests.request') as mock_request:
            TestMangaCollecAPIClient._setup_request_mock(mock_request)
            result = client._call_request("GET", "test/endpoint")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            method_arg, url_arg = TestMangaCollecAPIClient._extract_call_args(call_args)
            
            assert method_arg == "GET"
            assert url_arg == f"{MangaCollecAPIClient.BASE_URL}test/endpoint"
            assert call_args[1]['headers']['Authorization'] == f"{client.token_type} {client.access_token}"
            assert call_args[1]['proxies'] is None
            assert result == {"status": "success"}

    @patch('requests.post')
    def test_get_method(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        with patch.object(client, '_call_request') as mock_call_request:
            mock_call_request.return_value = {"data": "test"}

            params = {"param1": "value1"}
            result = client.get("test/endpoint", params=params)

            mock_call_request.assert_called_once_with("GET", "test/endpoint", params=params)
            assert result == {"data": "test"}

    @patch('requests.post')
    def test_post_method(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        with patch.object(client, '_call_request') as mock_call_request:
            mock_call_request.return_value = {"created": True}

            data = {"field1": "value1"}
            result = client.post("test/endpoint", data=data)

            mock_call_request.assert_called_once_with("POST", "test/endpoint", json=data)
            assert result == {"created": True}

    @patch('requests.post')
    def test_delete_method(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        with patch.object(client, '_call_request') as mock_call_request:
            mock_call_request.return_value = {"deleted": True}

            result = client.delete("test/endpoint")

            mock_call_request.assert_called_once_with("DELETE", "test/endpoint")
            assert result == {"deleted": True}

    @patch('requests.post')
    def test_call_request_http_error(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "created_at": int(time.time()),
            "expires_in": 3600
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = MangaCollecAPIClient(self.client_id, self.client_secret)

        with patch('requests.request') as mock_request:
            mock_request_response = Mock()
            mock_request_response.raise_for_status.side_effect = requests.exceptions.HTTPError("HTTP Error")
            mock_request.return_value = mock_request_response

            with pytest.raises(requests.exceptions.HTTPError):
                client._call_request("GET", "test/endpoint")

    @patch('requests.post')
    def test_authenticate_http_error(self, mock_post):
        mock_post.side_effect = requests.exceptions.HTTPError("Authentication failed")

        with pytest.raises(ConnectionError):
            MangaCollecAPIClient(self.client_id, self.client_secret)
