from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.job.entity.job import Job


class JobConverter(IConverterEntity[Job]):
    def serialize(self, model: Job) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        return {
            "id": model.id,
            "title": model.title
        }

    def deserialize(self, data: Dict) -> Job:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Job(
            id=data["id"],
            title=data["title"]
        )