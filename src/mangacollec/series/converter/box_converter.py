from typing import Dict, Any
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.series.entity.box import Box


class BoxConverter(IConverterEntity[Box]):
    """
    Convertisseur pour les entités Box.
    """

    def serialize(self, entity: Box) -> Dict[str, Any]:
        """
        Sérialise une entité Box en dictionnaire.
        
        :param entity: Entité Box à sérialiser
        :return: Dictionnaire représentant l'entité
        """
        return {
            "id": entity.id,
            "title": entity.title,
            "number": entity.number,
            "release_date": entity.release_date,
            "isbn": entity.isbn,
            "asin": entity.asin,
            "commercial_stop": entity.commercial_stop,
            "box_edition_id": entity.box_edition_id,
            "box_possessions_count": entity.box_possessions_count,
            "image_url": entity.image_url
        }

    def deserialize(self, data: Dict[str, Any]) -> Box:
        """
        Désérialise un dictionnaire en entité Box.
        
        :param data: Dictionnaire contenant les données du coffret
        :return: Entité Box
        """
        return Box(
            id=data["id"],
            title=data.get("title"),
            number=data["number"],
            release_date=data.get("release_date"),
            isbn=data.get("isbn"),
            asin=data.get("asin"),
            commercial_stop=data.get("commercial_stop"),
            box_edition_id=data["box_edition_id"],
            box_possessions_count=data.get("box_possessions_count"),
            image_url=data.get("image_url")
        )