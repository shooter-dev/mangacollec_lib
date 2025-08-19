from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.genres.entity.genre import Genre


class GenreConverter(IConverterEntity[Genre]):
    def serialize(self, model: Genre) -> Dict:
        return {
            "id": model.id,
            "title": model.title,
            "to_display": model.to_display
        }

    def deserialize(self, data: Dict) -> Genre:
        return Genre(
            id=data["id"],
            title=data["title"],
            to_display=data["to_display"]
        )