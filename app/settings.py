import os

from pydantic import BaseModel, computed_field

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine.url import URL


env_file = ".env"
if os.getenv("ENV_MODE") == "nodocker":
    env_file = ".nodocker.env"

print(f'Using env file: {env_file}')

class DbSettings(BaseModel):
    superuser: str
    superuser_password: str
    engine: str
    username: str
    password: str
    host: str
    port: int
    name: str

    @computed_field
    @property
    def database_url(self) -> str:
        return URL.create(
            drivername=self.engine,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name,
        ).render_as_string(hide_password=False)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8", env_nested_delimiter="__", extra="ignore")
    app_port: int
    localhost_port: int
    db: DbSettings


SETTINGS = Settings()
