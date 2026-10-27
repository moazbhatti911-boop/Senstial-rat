from fastapi.testclient import TestClient

from server.main import app
from server.config import API_KEY

client = TestClient(app)


def test_enrollment():
    response = client.post(
        "/enrollment/",
        headers={"X-API-Key": API_KEY},
        json={
            "hostname": "test-device",
            "platform": "Linux",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["enrolled"] is True
    assert "device_id" in data