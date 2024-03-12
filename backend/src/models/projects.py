from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSON

from backend.database.base import BaseModel

class Project(BaseModel):
     __tablename__ = "project"
     id = Column("id", Integer, primary_key=True, autoincrement=True)
     name = Column("name", String(length=32), nullable=False)
     description = Column("description", Text, nullable=True)
     date_start = Column("date_start", DateTime, nullable=False)
     date_end = Column("date_end", DateTime, nullable=False)
     geo_json = Column("geo_json", JSON, nullable=False)

