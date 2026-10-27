from fastapi.testclient import TestClient

from server.main import app
from server.config import API_KEY

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_admin_rejects_missing_key():
    response = client.get("/admin/status")

    assert response.status_code == 401


def test_admin_accepts_valid_key():
    response = client.get(
        "/admin/status",
        headers={"X-API-Key": API_KEY},
    )

    assert response.status_code == 200