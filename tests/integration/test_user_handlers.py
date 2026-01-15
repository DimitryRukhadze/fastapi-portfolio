from sqlalchemy.exc import IntegrityError
import pytest

from uuid import UUID

from app.handlers import create_new_user
from app.db import get_db_session


class TestUserPOSTHandler:
    unique_user = {
        "name": "unique_user_1",
        "email": "test1@example.com",
        "password": "StrongPassword123"
    }

    def test_handler_positive(self):
        session = next(get_db_session())
        new_user = create_new_user(self.unique_user, session)
        assert new_user["name"] == self.unique_user["name"]
        assert new_user["email"] == self.unique_user["email"]
        assert "id" in new_user
        assert isinstance(new_user["id"], UUID)
        session.close()

    def test_handler_no_password(self):
        session = next(get_db_session())
        with pytest.raises(ValueError) as excinfo:
            create_new_user({"name": self.unique_user["name"], "email": self.unique_user["email"]}, session)
        assert str(excinfo.value) == "Password required"
        session.close()

    def test_duplicate_user(self):
        session = next(get_db_session())
        create_new_user(self.unique_user, session)
        with pytest.raises(IntegrityError) as excinfo:
            create_new_user(self.unique_user, session)
        assert not excinfo.value is None
        session.close()