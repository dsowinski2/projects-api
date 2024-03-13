from abc import ABC
from typing import Generic
from typing import List
from typing import TypeVar

from fastapi import HTTPException

from backend.src.repositories.base import BaseRepository
from backend.src.repositories.excepions import ObjectNotFoundException
from backend.src.utils.types import CreateType
from backend.src.utils.types import ModelType
from backend.src.utils.types import UpdateType

RepoType = TypeVar("RepoType", bound=BaseRepository)


def handle_exception(e: Exception):
    if isinstance(e, ObjectNotFoundException):
        raise HTTPException(status_code=404, detail="Not found.")
    print(e)
    raise HTTPException(status_code=500, detail="Internal server error.")


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            handle_exception(e)

    return wrapper


class BaseController(ABC, Generic[ModelType, UpdateType, CreateType, RepoType]):
    def __init__(self, repository: RepoType):
        self.repository = repository

    @exception_handler
    def list_objects(self) -> List[ModelType]:
        return self.repository.all()

    @exception_handler
    def get_object_by_id(self, id: str) -> ModelType:
        return self.repository.get_by_id(id)

    @exception_handler
    def update_object(self, id: str, data: UpdateType) -> ModelType:
        return self.repository.update(id, data)

    @exception_handler
    def delete_object(self, id: str) -> bool:
        self.repository.delete(id)
        return

    @exception_handler
    def create_object(self, data: CreateType) -> ModelType:
        return self.repository.create(data)
