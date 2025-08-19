from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.volumes.entity.volume import Volume


class VolumeConverter(IConverterEntity[Volume]):
    def serialize(self, model: Volume) -> Dict:
        return {
            "id": model.id,
            "title": model.title,
            "number": model.number,
            "release_date": model.release_date,
            "isbn": model.isbn,
            "asin": model.asin,
            "edition_id": model.edition_id,
            "possessions_count": model.possessions_count,
            "not_sold": model.not_sold,
            "image_url": model.image_url,
            "nb_pages": model.nb_pages,
            "content": model.content
        }

    def deserialize(self, data: Dict) -> Volume:
        return Volume(
            id=data["id"],
            title=data.get("title"),
            number=data["number"],
            release_date=data.get("release_date"),
            isbn=data.get("isbn"),
            asin=data.get("asin"),
            edition_id=data["edition_id"],
            possessions_count=data["possessions_count"],
            not_sold=data["not_sold"],
            image_url=data.get("image_url"),
            nb_pages=data.get("nb_pages"),
            content=data.get("content")
        )