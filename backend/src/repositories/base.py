from abc import ABC
from typing import Generic
from typing import List

from sqlalchemy.orm.session import Session

from backend.src.repositories.excepions import ObjectNotFoundException
from backend.src.utils.types import CreateType
from backend.src.utils.types import ModelType
from backend.src.utils.types import UpdateType


class BaseRepository(ABC, Generic[ModelType, UpdateType, CreateType]):
    model = None

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: str) -> ModelType:
        if obj := self.session.query(self.model).get(id):
            return obj
        raise ObjectNotFoundException()

    def list(self) -> List[ModelType]:
        query = self.session.query(self.model)
        return query.all()

    def create(self, data: CreateType) -> ModelType:
        obj = self.model(**data.model_dump(exclude_unset=True))
        self.session.add(obj)
        self.session.flush()
        return obj

    def update(self, id: str, data: UpdateType) -> ModelType:
        obj = self.get_object_for_update(id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(obj, key, value)
        self.session.add(obj)
        return obj

    def delete(self, id: str) -> bool:
        obj = self.get_by_id(id)
        self.session.delete(obj)
        return True

    def get_object_for_update(self, id: str):
        if (
            obj := self.session.query(self.model)
            .with_for_update()
            .filter_by(id=id)
            .first()
        ):
            return obj
        raise ObjectNotFoundException()
