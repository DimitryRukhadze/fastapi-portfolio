import os

from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


env_file = ".env"
if os.getenv("ENV_MODE") == "nodocker":
    env_file = ".nodocker.env"


class DbSettings(BaseModel):
    superuser: str
    superuser_password: str
    engine: str
    username: str
    password: str
    host: str
    port: int
    name: str


class TestDbSettings(BaseModel):
    user: str
    password: str
    host: str
    port: int
    name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8", env_nested_delimiter="__", extra="ignore")
    app_port: int
    localhost_port: int
    db: DbSettings
    test_db: TestDbSettings

SETTINGS = Settings()
