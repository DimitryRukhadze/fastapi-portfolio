from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseModel):
    engine: str
    username: str
    password: str
    host: str
    port: int
    name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_nested_delimiter="__", extra="ignore")
    app_port: int
    localhost_port: int
    db: DbSettings
