from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import JSON

from .mixin import TimestampMixin
from backend.database.base import Base


class Project(Base, TimestampMixin):
    __tablename__ = "project"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(length=32), nullable=False)
    description = Column("description", Text, nullable=True)
    date_start = Column("date_start", DateTime, nullable=False)
    date_end = Column("date_end", DateTime, nullable=False)
    geo_json = Column("geo_json", JSON, nullable=False)
