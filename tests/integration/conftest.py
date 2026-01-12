import pytest

from sqlalchemy import text
from sqlalchemy_utils import create_database, database_exists, drop_database
from alembic import command
from alembic.config import Config
from app.settings import SETTINGS
from app.db import init_db, get_db_session


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    SETTINGS.db.name = "test_db"
    test_db_url = SETTINGS.db.database_url
    test_engine = init_db(SETTINGS.db.database_url)
    print(f'Setting up test database at: {test_db_url}')

    if database_exists(test_db_url):
        print('DROPPING AN EXISTING DB ONSTARTUP')
        drop_database(test_db_url)
    create_database(test_db_url)

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print('Test database setup complete.')

    yield

    test_engine.dispose()
    drop_database(test_db_url)
    print('Test database dropped.')
