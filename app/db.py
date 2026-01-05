from sqlalchemy import create_engine, text

from settings import Settings

settings = Settings()
db_settings = settings.db

engine = create_engine(f'{db_settings.engine}://{db_settings.username}:{db_settings.password}@{db_settings.host}:{db_settings.port}/{db_settings.name}', echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 'Hello, World!'"))
    print(result.all())
