from sqlalchemy.orm.session import Session


from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SessionLocal = sessionmaker[Session](autocommit=False, autoflush=False)


class DbBase(DeclarativeBase):
    pass


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
