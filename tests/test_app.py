from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_participant():
    response = client.post("/activities/Chess Club/signup?email=test@example.com")
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@example.com for Chess Club"

def test_unregister_participant():
    client.post("/activities/Chess Club/signup?email=test@example.com")  # Ensure participant is registered
    response = client.delete("/activities/Chess Club/unregister?email=test@example.com")
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered test@example.com from Chess Club"