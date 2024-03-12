class BaseRepositoryException(Exception):
    message: str = "Internal exception."
    def init(self, message):
        super.__init__(message)

class ObjectNotFoundException(BaseRepositoryException):
    message: str = "Not found."
