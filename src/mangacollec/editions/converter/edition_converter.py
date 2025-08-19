from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.editions.entity.edition import Edition


class EditionConverter(IConverterEntity[Edition]):
    def serialize(self, model: Edition) -> Dict:
        return {
            "id": model.id,
            "title": model.title,
            "series_id": model.series_id,
            "publisher_id": model.publisher_id,
            "parent_edition_id": model.parent_edition_id,
            "volumes_count": model.volumes_count,
            "last_volume_number": model.last_volume_number,
            "commercial_stop": model.commercial_stop,
            "not_finished": model.not_finished,
            "follow_editions_count": model.follow_editions_count
        }

    def deserialize(self, data: Dict) -> Edition:
        return Edition(
            id=data["id"],
            title=data.get("title"),
            series_id=data["series_id"],
            publisher_id=data["publisher_id"],
            parent_edition_id=data.get("parent_edition_id"),
            volumes_count=data["volumes_count"],
            last_volume_number=data.get("last_volume_number"),
            commercial_stop=data["commercial_stop"],
            not_finished=data["not_finished"],
            follow_editions_count=data["follow_editions_count"]
        )