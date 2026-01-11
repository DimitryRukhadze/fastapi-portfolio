import pytest

from uuid import UUID

from app.handlers import create_new_user


class TestUserPOSTHandler:
    unique_user = {
        "name": "unique_user",
        "email": "test@example.com"
    }

    def test_db_phase(self):
        new_user = create_new_user(self.unique_user)
        assert new_user["name"] == self.unique_user["name"]
        assert new_user["email"] == self.unique_user["email"]
        assert "id" in new_user
        assert isinstance(new_user["id"], UUID)
        print(new_user)
    
    def test_duplicate_user(self):
        with pytest.raises(Exception) as excinfo:
            new_user = create_new_user(self.unique_user)
        assert not new_user, "Expected an exception for duplicate user creation"
        print(new_user)

