from sqlalchemy import Column, Integer

from backend.database.base import BaseModel

class Project(BaseModel):
     __tablename__ = "project"
     id = Column("id", Integer, primary_key=True, autoincrement=True)