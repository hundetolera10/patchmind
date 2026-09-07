from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "PatchMind"
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_analyze_repository():
    response = client.post(
        "/analyze",
        json={
            "repository_path": "C:/projects/my-app",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["repository_path"] == "C:/projects/my-app"
    assert data["status"] == "queued"


def test_analyze_rejects_empty_repository_path():
    response = client.post(
        "/analyze",
        json={
            "repository_path": "",
        },
    )

    assert response.status_code == 422


def test_analyze_rejects_missing_repository_path():
    response = client.post(
        "/analyze",
        json={},
    )

    assert response.status_code == 422


def test_create_project():
    response = client.post(
        "/projects",
        json={
            "name": "broken-calculator",
            "repository_path": "C:/projects/broken-calculator",
            "language": "python",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["message"] == "project created"
    assert data["project"]["name"] == "broken-calculator"


def test_get_project():
    response = client.get("/projects/5")

    assert response.status_code == 200
    assert response.json()["project_id"] == 5


def test_project_language_filter():
    response = client.get("/projects?language=python")

    assert response.status_code == 200
    assert response.json()["language_filter"] == "python"

def test_create_project_rejects_empty_name():
    response = client.post(
        "/projects",
        json={
            "name": "",
            "repository_path": "C:/projects/test",
            "language": "python",
        },
    )

    assert response.status_code == 422

def test_invalid_project_id():
    response = client.get("/projects/hello")
    assert response.status_code == 422
