from sqlalchemy.exc import IntegrityError
import pytest
from pydantic import ValidationError
from uuid import UUID

from app.modules.auth.handlers import create_new_user
from app.core.database import get_db_session
from app.modules.auth.schemas import UserSchema, CreateUserSchema


class TestUserPOSTHandler:
    unique_user = CreateUserSchema(
        name="unique_user_1",
        email="test1@example.com",
        password="StrongPassword123"
    )

    def test_handler_positive(self):
        session = next(get_db_session())
        new_user = create_new_user(self.unique_user, session)
        assert new_user.username == self.unique_user.name
        assert new_user.email == self.unique_user.email
        assert new_user.id is not None
        assert isinstance(new_user.id, UUID)
        session.close()

    def test_handler_no_password(self):
        session = next(get_db_session())
        with pytest.raises(ValidationError) as excinfo:
            create_new_user(CreateUserSchema(name=self.unique_user.name, email=self.unique_user.email, password=''), session)
        assert excinfo.value.errors()[0]["type"] == "value_error"
        assert excinfo.value.errors()[0]["msg"] == "Value error, Password required"
        assert excinfo.value.errors()[0]["loc"] == ("password",)
        session.close()

    def test_duplicate_user(self):
        session = next(get_db_session())
        create_new_user(self.unique_user, session)
        with pytest.raises(IntegrityError) as excinfo:
            create_new_user(CreateUserSchema(
                name=self.unique_user.name,
                email=self.unique_user.email,
                password=self.unique_user.password
                ),
                session
            )
        assert not excinfo.value is None
        session.close()