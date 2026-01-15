import uuid

from sqlalchemy import Engine, String, create_engine, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


class DbBase(DeclarativeBase):
    pass


class User(DbBase):
    __tablename__ = 'user'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False)


def init_db(db_url: str) -> Engine:
    engine = create_engine(db_url, future=True)
    SessionLocal.configure(bind=engine)
    return engine


def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()