from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.author.entity.author import Author


class AuthorConverter(IConverterEntity[Author]):
    def serialize(self, model: Author) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        return {
            "id": model.id,
            "name": model.name,
            "first_name": model.first_name,
            "tasks_count": model.tasks_count
        }

    def deserialize(self, data: Dict) -> Author:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Author(
            id=data["id"],
            name=data["name"],
            first_name=data["first_name"],
            tasks_count=data["tasks_count"],
        )
