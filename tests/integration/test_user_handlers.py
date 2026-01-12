from sqlalchemy.exc import IntegrityError
import pytest

from uuid import UUID

from app.handlers import create_new_user
from app.db import get_db_session


class TestUserPOSTHandler:
    unique_user = {
        "name": "unique_user_1",
        "email": "test1@example.com"
    }

    def test_db_phase(self):
        session = next(get_db_session())
        new_user = create_new_user(self.unique_user, session)
        assert new_user["name"] == self.unique_user["name"]
        assert new_user["email"] == self.unique_user["email"]
        assert "id" in new_user
        assert isinstance(new_user["id"], UUID)
        session.close()
        print(new_user)
    
    def test_duplicate_user(self):
        with pytest.raises(IntegrityError) as excinfo:
            session = next(get_db_session())
            create_new_user(self.unique_user, session)
        assert not excinfo.value is None
        session.close()