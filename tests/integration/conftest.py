import pytest

from sqlalchemy_utils import create_database, database_exists, drop_database
from alembic import command
from alembic.config import Config
from app.settings import SETTINGS


TEST_DB_SETTINGS = SETTINGS.test_db
TEST_DB_URL=f'postgresql+psycopg2://{TEST_DB_SETTINGS.user}:{TEST_DB_SETTINGS.password}@{TEST_DB_SETTINGS.host}:{TEST_DB_SETTINGS.port}/{TEST_DB_SETTINGS.name}'


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    if not database_exists(TEST_DB_URL):
        create_database(TEST_DB_URL)
    
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print('Test database setup complete.')

    yield

    drop_database(TEST_DB_URL)
    print('Test database dropped.')
