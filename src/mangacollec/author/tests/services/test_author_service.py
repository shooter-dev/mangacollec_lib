import pytest
from unittest.mock import Mock, patch
from mangacollec.author.entity.author import Author
from mangacollec.author.services.author_service import AuthorService
from mangacollec.author.exception.author_exceptions import AuthorNotFoundError, AuthorValidationError, AuthorError


class TestAuthorService:
    """Tests pour le service AuthorService."""
    
    def setup_method(self):
        """Configuration avant chaque test."""
        self.mock_endpoint = Mock()
        self.service = AuthorService(self.mock_endpoint)
        
        # Auteurs de test
        self.test_authors = [
            Author(id="1", name="Oda", first_name="Eiichiro", tasks_count=42),
            Author(id="2", name="Toriyama", first_name="Akira", tasks_count=30),
            Author(id="3", name="Kubo", first_name="Tite", tasks_count=15)
        ]
    
    @patch('mangacollec.author.services.author_service.GetAuthorUseCase')
    def test_get_author_by_id_success(self, mock_get_usecase_class):
        """Test de la récupération réussie d'un auteur par ID."""
        # Arrange
        mock_usecase = Mock()
        mock_get_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = self.test_authors[0]
        
        # Act
        result = self.service.get_author_by_id("1")
        
        # Assert
        assert result == self.test_authors[0]
        mock_usecase.execute.assert_called_once_with("1")
    
    @patch('mangacollec.author.services.author_service.GetAuthorUseCase')
    def test_get_author_by_id_not_found(self, mock_get_usecase_class):
        """Test du cas où l'auteur n'est pas trouvé."""
        # Arrange
        mock_usecase = Mock()
        mock_get_usecase_class.return_value = mock_usecase
        mock_usecase.execute.side_effect = AuthorNotFoundError("999")
        
        # Act & Assert
        with pytest.raises(AuthorNotFoundError):
            self.service.get_author_by_id("999")
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_get_all_authors_success(self, mock_list_usecase_class):
        """Test de la récupération de tous les auteurs."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = self.test_authors
        
        # Act
        result = self.service.get_all_authors()
        
        # Assert
        assert result == self.test_authors
        mock_usecase.execute.assert_called_once_with(None, None)
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_get_all_authors_with_filters(self, mock_list_usecase_class):
        """Test de la récupération avec filtres."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = [self.test_authors[0]]
        
        # Act
        result = self.service.get_all_authors(name_filter="Oda", min_tasks=30)
        
        # Assert
        assert result == [self.test_authors[0]]
        mock_usecase.execute.assert_called_once_with("Oda", 30)
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_search_authors_by_name_success(self, mock_list_usecase_class):
        """Test de la recherche d'auteurs par nom."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = [self.test_authors[0]]
        
        # Act
        result = self.service.search_authors_by_name("Oda")
        
        # Assert
        assert result == [self.test_authors[0]]
        mock_usecase.execute.assert_called_once_with("Oda", None)
    
    def test_search_authors_by_name_empty_term(self):
        """Test de la recherche avec un terme vide."""
        # Act
        result = self.service.search_authors_by_name("")
        
        # Assert
        assert result == []
    
    def test_search_authors_by_name_whitespace_term(self):
        """Test de la recherche avec seulement des espaces."""
        # Act
        result = self.service.search_authors_by_name("   ")
        
        # Assert
        assert result == []
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_get_active_authors_default(self, mock_list_usecase_class):
        """Test de la récupération des auteurs actifs avec valeur par défaut."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        active_authors = [self.test_authors[0], self.test_authors[1]]
        mock_usecase.execute.return_value = active_authors
        
        # Act
        result = self.service.get_active_authors()
        
        # Assert
        assert result == active_authors
        mock_usecase.execute.assert_called_once_with(None, 1)
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_get_active_authors_custom_min(self, mock_list_usecase_class):
        """Test de la récupération des auteurs actifs avec un minimum personnalisé."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = [self.test_authors[0]]
        
        # Act
        result = self.service.get_active_authors(min_tasks=40)
        
        # Assert
        assert result == [self.test_authors[0]]
        mock_usecase.execute.assert_called_once_with(None, 40)
    
    @patch('mangacollec.author.services.author_service.GetAuthorUseCase')
    def test_get_author_display_name_success(self, mock_get_usecase_class):
        """Test de la récupération du nom d'affichage."""
        # Arrange
        mock_usecase = Mock()
        mock_get_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = self.test_authors[0]
        
        # Act
        result = self.service.get_author_display_name("1")
        
        # Assert
        expected_display_name = str(self.test_authors[0])  # "Oda Eiichiro"
        assert result == expected_display_name
        mock_usecase.execute.assert_called_once_with("1")
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_count_authors_success(self, mock_list_usecase_class):
        """Test du comptage des auteurs."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = self.test_authors
        
        # Act
        result = self.service.count_authors()
        
        # Assert
        assert result == 3
        mock_usecase.execute.assert_called_once_with(None, None)
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_count_authors_empty_list(self, mock_list_usecase_class):
        """Test du comptage avec une liste vide."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        mock_usecase.execute.return_value = []
        
        # Act
        result = self.service.count_authors()
        
        # Assert
        assert result == 0
    
    def test_service_initialization(self):
        """Test de l'initialisation du service."""
        # Assert
        assert self.service.authors_endpoint == self.mock_endpoint
        assert self.service.get_author_usecase is not None
        assert self.service.list_authors_usecase is not None
    
    @patch('mangacollec.author.services.author_service.GetAuthorUseCase')
    def test_get_author_by_id_validation_error_propagation(self, mock_get_usecase_class):
        """Test que les erreurs de validation sont propagées."""
        # Arrange
        mock_usecase = Mock()
        mock_get_usecase_class.return_value = mock_usecase
        validation_error = AuthorValidationError("id", "", "ID requis")
        mock_usecase.execute.side_effect = validation_error
        
        # Act & Assert
        with pytest.raises(AuthorValidationError):
            self.service.get_author_by_id("")
    
    @patch('mangacollec.author.services.author_service.ListAuthorsUseCase')
    def test_get_all_authors_error_propagation(self, mock_list_usecase_class):
        """Test que les erreurs des use cases sont propagées."""
        # Arrange
        mock_usecase = Mock()
        mock_list_usecase_class.return_value = mock_usecase
        author_error = AuthorError("Erreur API")
        mock_usecase.execute.side_effect = author_error
        
        # Act & Assert
        with pytest.raises(AuthorError):
            self.service.get_all_authors()
    
    def test_search_authors_by_name_none_term(self):
        """Test de la recherche avec un terme None."""
        # Act
        result = self.service.search_authors_by_name(None)
        
        # Assert
        assert result == []