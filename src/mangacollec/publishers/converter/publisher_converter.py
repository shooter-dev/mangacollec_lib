from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.publishers.entity.publisher import Publisher


class PublisherConverter(IConverterEntity[Publisher]):
    def serialize(self, model: Publisher) -> Dict:
        return {
            "id": model.id,
            "title": model.title,
            "closed": model.closed,
            "editions_count": model.editions_count,
            "no_amazon": model.no_amazon
        }

    def deserialize(self, data: Dict) -> Publisher:
        return Publisher(
            id=data["id"],
            title=data["title"],
            closed=data["closed"],
            editions_count=data["editions_count"],
            no_amazon=data["no_amazon"]
        )