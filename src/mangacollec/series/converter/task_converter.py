from typing import Dict, Any
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.series.entity.task import Task


class TaskConverter(IConverterEntity[Task]):
    """
    Convertisseur pour les entités Task.
    """

    def serialize(self, entity: Task) -> Dict[str, Any]:
        """
        Sérialise une entité Task en dictionnaire.
        
        :param entity: Entité Task à sérialiser
        :return: Dictionnaire représentant l'entité
        """
        return {
            "id": entity.id,
            "job_id": entity.job_id,
            "series_id": entity.series_id,
            "author_id": entity.author_id
        }

    def deserialize(self, data: Dict[str, Any]) -> Task:
        """
        Désérialise un dictionnaire en entité Task.
        
        :param data: Dictionnaire contenant les données de la tâche
        :return: Entité Task
        """
        return Task(
            id=data["id"],
            job_id=data["job_id"],
            series_id=data["series_id"],
            author_id=data["author_id"]
        )