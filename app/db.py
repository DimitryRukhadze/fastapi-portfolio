from pydantic import UUID5

from sqlalchemy import String, create_engine, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .settings import SETTINGS


DB_SETTINGS = SETTINGS.db
DB_URL = f'{DB_SETTINGS.engine}://{DB_SETTINGS.username}:{DB_SETTINGS.password}@{DB_SETTINGS.host}:{DB_SETTINGS.port}/{DB_SETTINGS.name}'
ENGINE = create_engine(DB_URL, echo=True)


class DbBase(DeclarativeBase):
    pass


class User(DbBase):
    __tablename__ = 'user'

    id: Mapped[UUID5] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]
