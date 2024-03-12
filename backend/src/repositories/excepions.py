from enum import Enum


class BaseRepositoryException(Exception):
    message: str = "Internal exception."
    def init(self, message):
        super.__init__(message)

class BaseRepositoryExceptions(Enum):
    OBJECT_NOT_FOUND = "OBJECT_NOT_FOUND"
    