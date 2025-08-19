from typing import Dict, Any
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.series.entity.box_edition import BoxEdition


class BoxEditionConverter(IConverterEntity[BoxEdition]):
    """
    Convertisseur pour les entités BoxEdition.
    """

    def serialize(self, entity: BoxEdition) -> Dict[str, Any]:
        """
        Sérialise une entité BoxEdition en dictionnaire.
        
        :param entity: Entité BoxEdition à sérialiser
        :return: Dictionnaire représentant l'entité
        """
        return {
            "id": entity.id,
            "title": entity.title,
            "publisher_id": entity.publisher_id,
            "boxes_count": entity.boxes_count,
            "adult_content": entity.adult_content,
            "box_follow_editions_count": entity.box_follow_editions_count
        }

    def deserialize(self, data: Dict[str, Any]) -> BoxEdition:
        """
        Désérialise un dictionnaire en entité BoxEdition.
        
        :param data: Dictionnaire contenant les données de l'édition de coffrets
        :return: Entité BoxEdition
        """
        return BoxEdition(
            id=data["id"],
            title=data["title"],
            publisher_id=data["publisher_id"],
            boxes_count=data["boxes_count"],
            adult_content=data["adult_content"],
            box_follow_editions_count=data["box_follow_editions_count"]
        )