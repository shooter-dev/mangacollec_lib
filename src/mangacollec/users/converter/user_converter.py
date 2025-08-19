from typing import Dict
from mangacollec.core.interfaces.converter_interface import IConverterEntity
from mangacollec.users.entity.user import User


class UserConverter(IConverterEntity[User]):
    def serialize(self, model: User) -> Dict:
        return {
            "username": model.username,
            "collection": model.collection
        }

    def deserialize(self, data: Dict) -> User:
        return User(
            username=data["username"],
            collection=data.get("collection")
        )