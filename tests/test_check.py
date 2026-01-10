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