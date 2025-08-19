import pytest
from unittest.mock import Mock, MagicMock
from mangacollec.author.entity.author import Author
from mangacollec.author.usecases.get_author_usecase import GetAuthorUseCase
from mangacollec.author.responses.author_response import AuthorEndpointResponse
from mangacollec.author.exception.author_exceptions import AuthorNotFoundError, AuthorValidationError


class TestGetAuthorUseCase:
    """Tests pour le use case GetAuthorUseCase."""
    
    def setup_method(self):
        """Configuration avant chaque test."""
        self.mock_endpoint = Mock()
        self.usecase = GetAuthorUseCase(self.mock_endpoint)
        
        # Auteur de test
        self.test_author = Author(
            id="123",
            name="Oda",
            first_name="Eiichiro",
            tasks_count=42
        )
    
    def test_execute_success(self):
        """Test de la récupération réussie d'un auteur."""
        # Arrange
        author_id = "123"
        response = AuthorEndpointResponse(authors=[self.test_author])
        self.mock_endpoint.get_by_id_v2.return_value = response
        
        # Act
        result = self.usecase.execute(author_id)
        
        # Assert
        assert result == self.test_author
        self.mock_endpoint.get_by_id_v2.assert_called_once_with(author_id)
    
    def test_execute_author_not_found(self):
        """Test du cas où l'auteur n'existe pas."""
        # Arrange
        author_id = "999"
        response = AuthorEndpointResponse(authors=[])
        self.mock_endpoint.get_by_id_v2.return_value = response
        
        # Act & Assert
        with pytest.raises(AuthorNotFoundError) as exc_info:
            self.usecase.execute(author_id)
        
        assert str(exc_info.value) == "Auteur avec l'ID '999' introuvable."
        assert exc_info.value.author_id == author_id
    
    def test_execute_empty_author_id(self):
        """Test avec un ID d'auteur vide."""
        # Act & Assert
        with pytest.raises(AuthorValidationError) as exc_info:
            self.usecase.execute("")
        
        assert "L'ID de l'auteur est requis" in str(exc_info.value)
        assert exc_info.value.field == "author_id"
    
    def test_execute_none_author_id(self):
        """Test avec un ID d'auteur None."""
        # Act & Assert
        with pytest.raises(AuthorValidationError) as exc_info:
            self.usecase.execute(None)
        
        assert "L'ID de l'auteur est requis" in str(exc_info.value)
    
    def test_execute_whitespace_author_id(self):
        """Test avec un ID d'auteur contenant seulement des espaces."""
        # Act & Assert
        with pytest.raises(AuthorValidationError) as exc_info:
            self.usecase.execute("   ")
        
        assert "L'ID ne peut pas être vide" in str(exc_info.value)
    
    def test_execute_non_string_author_id(self):
        """Test avec un ID d'auteur qui n'est pas une chaîne."""
        # Act & Assert
        with pytest.raises(AuthorValidationError) as exc_info:
            self.usecase.execute(123)
        
        assert "L'ID doit être une chaîne de caractères" in str(exc_info.value)
    
    def test_execute_multiple_authors_returned(self):
        """Test du cas où plusieurs auteurs sont retournés (ne devrait pas arriver)."""
        # Arrange
        author_id = "123"
        second_author = Author(
            id="456",
            name="Toriyama",
            first_name="Akira",
            tasks_count=30
        )
        response = AuthorEndpointResponse(authors=[self.test_author, second_author])
        self.mock_endpoint.get_by_id_v2.return_value = response
        
        # Act
        result = self.usecase.execute(author_id)
        
        # Assert - Doit retourner le premier auteur
        assert result == self.test_author
    
    def test_validation_called_before_endpoint(self):
        """Test que la validation est appelée avant l'endpoint."""
        # Act & Assert
        with pytest.raises(AuthorValidationError):
            self.usecase.execute("")
        
        # L'endpoint ne doit pas être appelé si la validation échoue
        self.mock_endpoint.get_by_id_v2.assert_not_called()
    
    def test_execute_with_valid_id_strip(self):
        """Test avec un ID valide mais avec des espaces à supprimer."""
        # Arrange
        author_id = "  123  "
        response = AuthorEndpointResponse(authors=[self.test_author])
        self.mock_endpoint.get_by_id_v2.return_value = response
        
        # Act
        result = self.usecase.execute(author_id)
        
        # Assert
        assert result == self.test_author
        # L'endpoint doit être appelé avec l'ID original (non strippé)
        self.mock_endpoint.get_by_id_v2.assert_called_once_with(author_id)