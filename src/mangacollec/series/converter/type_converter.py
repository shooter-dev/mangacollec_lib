from typing import Dict, Any
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.series.entity.type import Type


class TypeConverter(IConverterEntity[Type]):
    """
    Convertisseur pour les entités Type.
    """

    def serialize(self, entity: Type) -> Dict[str, Any]:
        """
        Sérialise une entité Type en dictionnaire.
        
        :param entity: Entité Type à sérialiser
        :return: Dictionnaire représentant l'entité
        """
        return {
            "id": entity.id,
            "title": entity.title,
            "to_display": entity.to_display
        }

    def deserialize(self, data: Dict[str, Any]) -> Type:
        """
        Désérialise un dictionnaire en entité Type.
        
        :param data: Dictionnaire contenant les données du type
        :return: Entité Type
        """
        return Type(
            id=data["id"],
            title=data["title"],
            to_display=data["to_display"]
        )