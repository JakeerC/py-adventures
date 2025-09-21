from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    """Settings class docstring..."""

    API_PREFIX: str = "/api"
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite://:memory:"
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
