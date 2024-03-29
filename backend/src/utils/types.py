from datetime import datetime
from typing import Annotated
from typing import TypeVar

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import StringConstraints


ModelType = TypeVar("ModelType")
UpdateType = TypeVar("UpdateType", bound=BaseModel)
CreateType = TypeVar("CreateType", bound=BaseModel)


class ProjectIdType(BaseModel):
    id: int


class ProjectCreateType(BaseModel):
    name: Annotated[str, StringConstraints(max_length=32)]
    description: str | None = None
    date_start: datetime
    date_end: datetime
    geo_json: dict

    model_config = ConfigDict(from_attributes=True)


class ProjectType(ProjectCreateType, ProjectIdType):
    pass


class ProjectUpdateType(BaseModel):
    name: str | None = None
    description: str | None = None
    date_start: datetime | None = None
    date_end: datetime | None = None
    geo_json: dict | None = None

    model_config = ConfigDict(from_attributes=True)
