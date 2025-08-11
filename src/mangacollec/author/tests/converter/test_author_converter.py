from typing import Dict

import pytest
from pydantic import ValidationError

from mangacollec.author.converter.author_converter import AuthorConverter
from mangacollec.author.entity.author import Author


class TestAuthorConverter:

    def setup_method(self):
        """Configuration du convertisseur pour les tests."""
        self.converter = AuthorConverter()

    def test_deserialize_complete_author(self):
        """Test de désérialisation d'un author complète."""

        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32
        }

        author: Author = self.converter.deserialize(data)

        assert isinstance(author, Author)

        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"
        assert author.first_name == "Masashi"
        assert author.tasks_count == 32

    def test_deserialize_author_with_empty_first_name(self):
        """Test de désérialisation d'un author avec 'first_name' a null"""

        data = {
            "id": "13dfa960-ba31-40a2-9d46-387807a4f70f",
            "name": "One",
            "first_name": "",
            "tasks_count": 5
        }

        author: Author = self.converter.deserialize(data)

        assert isinstance(author, Author)

        assert author.id == "13dfa960-ba31-40a2-9d46-387807a4f70f"
        assert author.name == "One"
        assert author.first_name == ""
        assert author.tasks_count == 5

    def test_deserialize_with_missing_field(self):
        """Test de désérialisation avec un champ manquant."""

        data = {
            "id": "13dfa960-ba31-40a2-9d46-387807a4f70f",
            "name": "One",
            "first_name": "",
            # "tasks_count" manquant
        }

        with pytest.raises(KeyError):
            self.converter.deserialize(data)

    def test_deserialize_with_none_data(self):
        """Test de désérialisation avec données None."""

        with pytest.raises(TypeError):
            self.converter.deserialize(None)

    def test_deserialize_with_empty_dict(self):
        """Test de désérialisation avec dictionnaire vide."""

        data = {}

        with pytest.raises(KeyError):
            self.converter.deserialize(data)

    def test_deserialize_with_extra_fields(self):
        """Test avec champs supplémentaires ignorés."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32,
            "extra_field": "should_be_ignored"
        }

        author: Author = self.converter.deserialize(data)

        assert isinstance(author, Author)

        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"
        assert author.first_name == "Masashi"
        assert author.tasks_count == 32

    def test_deserialize_with_zero_tasks_count(self):
        """Test avec tasks_count à 0."""
        data = {
            "id": "619724eb-5748-4fa5-80ac-e8434218bbc9",
            "name": "Niwa",
            "first_name": "Haruki",
            "tasks_count": 0
        }

        author: Author = self.converter.deserialize(data)

        assert isinstance(author, Author)

        assert author.id == "619724eb-5748-4fa5-80ac-e8434218bbc9"
        assert author.name == "Niwa"
        assert author.first_name == "Haruki"
        assert author.tasks_count == 0

    def test_deserialize_with_invalid_types(self):
        """Test avec des types invalides."""
        data = {
            "id": 123,  # int au lieu de str
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": "32"  # str au lieu de int
        }

        with pytest.raises(ValidationError):
            self.converter.deserialize(data)

    def test_deserialize_with_negative_tasks_count(self):
        """Test avec tasks_count négatif."""
        data = {
            "id": "619724eb-5748-4fa5-80ac-e8434218bbc9",
            "name": "Niwa",
            "first_name": "Haruki",
            "tasks_count": -1
        }

        author: Author = self.converter.deserialize(data)

        assert isinstance(author, Author)

        assert author.id == "619724eb-5748-4fa5-80ac-e8434218bbc9"
        assert author.name == "Niwa"
        assert author.first_name == "Haruki"
        assert author.tasks_count == -1

    def test_serialize_complete_author(self):
        """Test de désérialisation d'un author complète."""

        author = Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32
        )

        data_dict = self.converter.serialize(author)

        assert isinstance(data_dict, Dict)

        assert data_dict["id"] == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert data_dict["name"] == "Kishimoto"
        assert data_dict["first_name"] == "Masashi"
        assert data_dict["tasks_count"] == 32

    def test_serialize_author_with_none_first_name(self):
        """Test de désérialisation d'un author complète."""

        author = Author(
            id="13dfa960-ba31-40a2-9d46-387807a4f70f",
            name="One",
            first_name=None,
            tasks_count=5
        )

        data_dict = self.converter.serialize(author)

        assert isinstance(data_dict, Dict)

        assert data_dict["id"] == "13dfa960-ba31-40a2-9d46-387807a4f70f"
        assert data_dict["name"] == "One"
        assert data_dict["first_name"] is None
        assert data_dict["tasks_count"] == 5

    def test_serialize_with_none_author(self):
        """Test de sérialisation avec Author None."""
        with pytest.raises(AttributeError):
            self.converter.serialize(None)
