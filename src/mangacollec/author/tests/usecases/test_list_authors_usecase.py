import pytest
from unittest.mock import Mock
from mangacollec.author.entity.author import Author
from mangacollec.author.usecases.list_authors_usecase import ListAuthorsUseCase
from mangacollec.author.responses.authors_response import AuthorsEndpointResponse
from mangacollec.author.exception.author_exceptions import AuthorError


class TestListAuthorsUseCase:
    """Tests pour le use case ListAuthorsUseCase."""
    
    def setup_method(self):
        """Configuration avant chaque test."""
        self.mock_endpoint = Mock()
        self.usecase = ListAuthorsUseCase(self.mock_endpoint)
        
        # Auteurs de test
        self.test_authors = [
            Author(id="1", name="Oda", first_name="Eiichiro", tasks_count=42),
            Author(id="2", name="Toriyama", first_name="Akira", tasks_count=30),
            Author(id="3", name="Kubo", first_name="Tite", tasks_count=15),
            Author(id="4", name="Kishimoto", first_name="Masashi", tasks_count=25),
            Author(id="5", name="Araki", first_name="Hirohiko", tasks_count=50)
        ]
    
    def test_execute_success_no_filters(self):
        """Test de la récupération réussie sans filtres."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute()
        
        # Assert
        assert len(result) == 5
        # Vérifier que les auteurs sont triés par nom
        assert result[0].title == "Araki"
        assert result[1].title == "Kishimoto"
        assert result[2].title == "Kubo"
        assert result[3].title == "Oda"
        assert result[4].title == "Toriyama"
        self.mock_endpoint.get_all_v2.assert_called_once()
    
    def test_execute_with_name_filter(self):
        """Test avec filtre par nom."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute(name_filter="oda")
        
        # Assert
        assert len(result) == 1
        assert result[0].title == "Oda"
    
    def test_execute_with_name_filter_first_name(self):
        """Test avec filtre sur le prénom."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute(name_filter="akira")
        
        # Assert
        assert len(result) == 1
        assert result[0].first_name == "Akira"
    
    def test_execute_with_min_tasks_filter(self):
        """Test avec filtre par nombre minimum de tâches."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute(min_tasks=30)
        
        # Assert
        assert len(result) == 3
        task_counts = [author.tasks_count for author in result]
        assert all(count >= 30 for count in task_counts)
    
    def test_execute_with_both_filters(self):
        """Test avec les deux filtres combinés."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute(name_filter="a", min_tasks=40)
        
        # Assert
        assert len(result) == 2  # Araki et Oda qui ont 'a' dans le nom et >= 40 tâches
        names = [author.title for author in result]
        assert "Araki" in names
        assert "Oda" in names
    
    def test_execute_no_results_with_filters(self):
        """Test avec des filtres qui ne donnent aucun résultat."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute(name_filter="xyz")
        
        # Assert
        assert len(result) == 0
    
    def test_execute_empty_response(self):
        """Test avec une réponse vide de l'endpoint."""
        # Arrange
        response = AuthorsEndpointResponse(authors=[])
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute()
        
        # Assert
        assert len(result) == 0
    
    def test_execute_endpoint_exception(self):
        """Test du cas où l'endpoint lève une exception."""
        # Arrange
        self.mock_endpoint.get_all_v2.side_effect = Exception("API Error")
        
        # Act & Assert
        with pytest.raises(AuthorError) as exc_info:
            self.usecase.execute()
        
        assert "Erreur lors de la récupération des auteurs" in str(exc_info.value)
    
    def test_execute_author_error_propagation(self):
        """Test que les AuthorError sont propagées sans modification."""
        # Arrange
        original_error = AuthorError("Erreur spécifique")
        self.mock_endpoint.get_all_v2.side_effect = original_error
        
        # Act & Assert
        with pytest.raises(AuthorError) as exc_info:
            self.usecase.execute()
        
        assert exc_info.value is original_error
    
    def test_name_filter_case_insensitive(self):
        """Test que le filtre par nom est insensible à la casse."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result_lower = self.usecase.execute(name_filter="oda")
        result_upper = self.usecase.execute(name_filter="ODA")
        result_mixed = self.usecase.execute(name_filter="Oda")
        
        # Assert
        assert len(result_lower) == len(result_upper) == len(result_mixed) == 1
        assert result_lower[0] == result_upper[0] == result_mixed[0]
    
    def test_name_filter_with_whitespace(self):
        """Test avec un filtre contenant des espaces."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute(name_filter="  oda  ")
        
        # Assert
        assert len(result) == 1
        assert result[0].title == "Oda"
    
    def test_sorting_by_name_and_first_name(self):
        """Test du tri par nom puis prénom."""
        # Arrange - Ajouter des auteurs avec le même nom
        authors_same_name = [
            Author(id="6", name="Oda", first_name="Eiichiro", tasks_count=42),
            Author(id="7", name="Oda", first_name="Akira", tasks_count=20)
        ]
        response = AuthorsEndpointResponse(authors=authors_same_name)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute()
        
        # Assert
        assert len(result) == 2
        assert result[0].first_name == "Akira"  # A vient avant E
        assert result[1].first_name == "Eiichiro"
    
    def test_author_without_first_name(self):
        """Test avec un auteur sans prénom."""
        # Arrange
        author_no_first_name = Author(id="8", name="Nameless", first_name=None, tasks_count=10)
        response = AuthorsEndpointResponse(authors=[author_no_first_name])
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute()
        
        # Assert
        assert len(result) == 1
        assert result[0].first_name is None
    
    def test_min_tasks_zero(self):
        """Test avec min_tasks=0 (doit inclure tous les auteurs)."""
        # Arrange
        response = AuthorsEndpointResponse(authors=self.test_authors)
        self.mock_endpoint.get_all_v2.return_value = response
        
        # Act
        result = self.usecase.execute(min_tasks=0)
        
        # Assert
        assert len(result) == 5  # Tous les auteurs