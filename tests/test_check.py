import pytest

from fastapi.testclient import TestClient

from app.main import app

class TestCheck:
    client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json().get("status", None) == "ok"
        assert response.json().get("message", None) is not None
    
    def test_db_health_check(self):
        response = self.client.get("/db_health")
        assert response.status_code == 200
        assert response.json().get("status", None) == "healthy"


class TestUsers:
    client = TestClient(app)

    def test_get_users(self):
        response = self.client.get("/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_create_user(self):
        new_user = {
            "name": "Test User",
            "email": "test@example.com"
        }
        response = self.client.post("/users", json=new_user)
        assert response.status_code == 200
        assert response.json().get("name", None) == new_user["name"]
        assert response.json().get("email", None) == new_user["email"]
        assert response.json().get("id", None) is not None
