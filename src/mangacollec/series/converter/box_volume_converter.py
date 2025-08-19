from typing import Dict, Any
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.series.entity.box_volume import BoxVolume


class BoxVolumeConverter(IConverterEntity[BoxVolume]):
    """
    Convertisseur pour les entités BoxVolume.
    """

    def serialize(self, entity: BoxVolume) -> Dict[str, Any]:
        """
        Sérialise une entité BoxVolume en dictionnaire.
        
        :param entity: Entité BoxVolume à sérialiser
        :return: Dictionnaire représentant l'entité
        """
        return {
            "id": entity.id,
            "box_id": entity.box_id,
            "volume_id": entity.volume_id,
            "included": entity.included
        }

    def deserialize(self, data: Dict[str, Any]) -> BoxVolume:
        """
        Désérialise un dictionnaire en entité BoxVolume.
        
        :param data: Dictionnaire contenant les données de la relation coffret-volume
        :return: Entité BoxVolume
        """
        return BoxVolume(
            id=data["id"],
            box_id=data["box_id"],
            volume_id=data["volume_id"],
            included=data["included"]
        )