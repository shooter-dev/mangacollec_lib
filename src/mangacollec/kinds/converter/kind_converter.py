from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.kinds.entity.kind import Kind


class KindConverter(IConverterEntity[Kind]):
    def serialize(self, model: Kind) -> Dict:
        return {
            "id": model.id,
            "title": model.title
        }

    def deserialize(self, data: Dict) -> Kind:
        return Kind(
            id=data["id"],
            title=data["title"]
        )