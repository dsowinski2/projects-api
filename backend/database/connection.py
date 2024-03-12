from sqlalchemy import create_engine
from sqlalchemy.engine import url

from backend.config import settings


db_url = None
db = None
url_params = {
    "drivername": "postgresql",
    "host": "postgresql",
    "port": 5432,
    "username": settings.POSTGRES_USER,
    "password": settings.POSTGRES_PASSWORD,
    "database": "db",
}
db_url = url.URL.create(**url_params)

db = create_engine(db_url)
