from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_owner_can_access_own_project():
    response = client.get("/projects/1", headers={"X-User-ID": "1"})
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["owner_id"] == 1
