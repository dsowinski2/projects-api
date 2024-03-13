import json

import pytest

from backend.config.server import app
from backend.database.session import db_session as app_db_session
from backend.src.models import Project


pytestmark = pytest.mark.usefixtures("db_session")


@pytest.fixture(autouse=True)
def override_db_session_dependency(db_session):
    app.dependency_overrides[app_db_session] = lambda: db_session
    return


def test_projects_listing_return_empty_list(api_client):
    response = api_client.get("/api/projects/")

    assert response.status_code == 200
    assert response.json() == []


def test_project_listing_returns_objects(api_client, project_factory):
    project_factory.create_batch(5)

    response = api_client.get("/api/projects/")

    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 5


def test_get_project_raises_404(api_client):
    response = api_client.get("/api/projects/1")

    response_data = response.json()
    assert response.status_code == 404
    assert response_data["detail"] == "Not found."


def test_get_project_success_response(api_client, project_factory):
    project = project_factory()

    response = api_client.get(f"/api/projects/{project.id}")

    response_data = response.json()
    assert response.status_code == 200
    assert response_data["id"] == project.id
    assert response_data["name"] == project.name
    assert response_data["description"] == project.description
    assert response_data["date_end"] == project.date_end.isoformat()
    assert response_data["date_start"] == project.date_start.isoformat()
    assert response_data["geo_json"] == project.geo_json


def test_delete_project_raises_404(api_client):
    response = api_client.delete("/api/projects/1")

    response_data = response.json()
    assert response.status_code == 404
    assert response_data["detail"] == "Not found."


def test_delete_project_success_response(api_client, project_factory, db_session):
    project = project_factory()

    response = api_client.delete(f"/api/projects/{project.id}")

    response_data = response.json()
    assert response.status_code == 200
    assert response_data is None
    assert db_session.query(Project).first() is None


def test_update_project_raises_404(api_client):
    response = api_client.patch(
        "/api/projects/1", data=json.dumps({"name": "new_name"})
    )

    response_data = response.json()
    assert response.status_code == 404
    assert response_data["detail"] == "Not found."


def test_update_project_success_response(api_client, project_factory):
    project = project_factory()
    response = api_client.patch(
        f"/api/projects/{project.id}", data=json.dumps({"name": "new_name"})
    )

    response_data = response.json()
    assert response.status_code == 200
    assert response_data["name"] == "new_name"


def test_create_project_success_response(api_client):
    data = {
        "description": "description",
        "name": "project_name",
        "date_end": "2019-01-13T16:46:34.914671",
        "date_start": "2019-01-13T16:46:34.914671",
        "geo_json": {"key": "value"},
    }
    response = api_client.post("/api/projects", data=json.dumps(data))

    response_data = response.json()
    assert response.status_code == 200
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert response_data["date_end"] == data["date_end"]
    assert response_data["date_start"] == data["date_start"]
    assert response_data["geo_json"] == data["geo_json"]
    assert response_data["id"]


def test_create_project_skip_optional_success_response(api_client):
    data = {
        "name": "project_name",
        "date_end": "2019-01-13T16:46:34.914671",
        "date_start": "2019-01-13T16:46:34.914671",
        "geo_json": {"key": "value"},
    }
    response = api_client.post("/api/projects", data=json.dumps(data))

    response_data = response.json()
    assert response.status_code == 200
    assert not response_data.get("description")
