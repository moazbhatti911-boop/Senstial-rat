from fastapi.testclient import TestClient

from server.main import app
from server.config import API_KEY

client = TestClient(app)


def test_allowed_action():
    response = client.post(
        "/actions/",
        headers={"X-API-Key": API_KEY},
        json={"action": "health_check"},
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_unknown_action_rejected():
    response = client.post(
        "/actions/",
        headers={"X-API-Key": API_KEY},
        json={"action": "unknown_action"},
    )

    assert response.status_code == 422