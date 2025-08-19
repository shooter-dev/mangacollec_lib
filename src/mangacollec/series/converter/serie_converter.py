from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.series.entity.serie import Serie


class SerieConverter(IConverterEntity[Serie]):
    def serialize(self, model: Serie) -> Dict:
        return {
            "id": model.id,
            "title": model.title,
            "type_id": model.type_id,
            "adult_content": model.adult_content,
            "editions_count": model.editions_count,
            "tasks_count": model.tasks_count,
            "kinds_ids": model.kinds_ids
        }

    def deserialize(self, data: Dict) -> Serie:
        return Serie(
            id=data["id"],
            title=data["title"],
            type_id=data["type_id"],
            adult_content=data["adult_content"],
            editions_count=data["editions_count"],
            tasks_count=data["tasks_count"],
            kinds_ids=data.get("kinds_ids")
        )