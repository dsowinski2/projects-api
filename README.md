# Project's API

## Tools/Frameworks:
* PostgreSQL
* FastAPI
* SQLAlchemy
* Alembic
* Docker
* Pytest


## Prerequisite
- Docker

## Setting up project:

```bash
git clone https://github.com/dsowinski2/projects-api.git
cd projects-api
cp .env.example .env
```
Set Postgres credential for both default and test database

```bash
docker compose run --rm backend alembic upgrade heads
```
Project should be running on http://localhost:5001

API: http://localhost:5001/api/projects

DOCS: http://localhost:5001/docs

## Run tests:

```bash
docker compose run --rm backend pytest
```

## Migrations:
[Alembic](https://alembic.sqlalchemy.org/en/latest/)

Generate new migration based on model class change:
```bash
docker compose run --rm backend alembic revision --autogenerate
```
Migrate database to latest state
```bash
docker compose run --rm backend alembic upgrade heads
```
Revert to specific migration
```bash
docker compose run --rm backend alembic downgrade <revision>
```

## Git hooks
This project has configured [pre-commit](https://pre-commit.com/) with following hooks:
* black
* flake8
* reorder-python-imports
Configure it by running:
```bash
pip install pre-commit
pre-commit install
```

 
