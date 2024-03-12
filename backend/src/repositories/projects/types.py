from datetime import datetime
from pydantic import BaseModel, Json
from typing import Any


class ProjectCreateType(BaseModel):
    name: str
    description: str | None = None
    date_start: datetime
    date_end: datetime
    geo_json: Json[Any]

class ProjectUpdateType(BaseModel):
    name: str | None = None
    description: str | None = None
    date_start: datetime | None = None
    date_end: datetime | None = None
    geo_json: Json[Any] | None = None
