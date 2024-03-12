from abc import ABC
from typing import Generic, List, TypeVar

from fastapi import HTTPException
from pydantic import BaseModel
from backend.src.repositories.base import BaseRepository
from backend.src.repositories.excepions import ObjectNotFoundException

from backend.src.utils.types import CreateType, ModelType, UpdateType

RepoType = TypeVar("RepoType", bound=BaseRepository)

def handle_exception(e: Exception):
        if isinstance(e, ObjectNotFoundException):
            raise HTTPException(status_code=404, detail="Not found.")
        raise HTTPException(status_code=500, detail="Internal server error.")

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            handle_exception(e)
    return wrapper

class BaseController(ABC, Generic[ModelType, UpdateType, CreateType, RepoType]):
    def __init__(self, repository: RepoType, data_model: BaseModel):
        self.repository = repository
        self.data_model = data_model

    @exception_handler
    def list_objects(self) -> List[ModelType]:
        return self.repository.list()
    
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
        return self.data_model.model_validate(self.repository.create(data))

    
