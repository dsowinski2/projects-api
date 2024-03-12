from abc import ABC
from typing import TypeVar, Generic, List

from pydantic import BaseModel
from sqlalchemy.orm.session import Session

from backend.src.repositories.excepions import BaseRepositoryException, BaseRepositoryExceptions


ModelType = TypeVar("ModelType")
UpdateType = TypeVar("UpdateType", bound=BaseModel)
CreateType = TypeVar("CreateType", bound=BaseModel)

class BaseRepository(ABC, Generic[ModelType, UpdateType, CreateType]):
    model = None

    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, id: str) -> ModelType:
        if obj := self.session.query(self.model).get(id):
            return obj
        raise BaseRepositoryException(BaseRepositoryExceptions.OBJECT_NOT_FOUND.value)

    def list(self) -> List[ModelType]:
        query = self.session.query(self.model)
        return query.all()
        
    def create(self, data: CreateType) -> ModelType:
        obj = self.model(**data.model_dump(exclude_unset=True))
        self.session.add(obj)
        return obj

    def update(self, id: str, data: UpdateType) -> ModelType:
        obj = self.get_by_id(id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(obj, key, value)
        self.session.add(obj)
        return obj


    def delete(self, id: str) -> bool:
        obj = self.get_by_id(id)
        obj.delete()
        return True
