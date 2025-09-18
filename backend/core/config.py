from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    ALLOWED_ORIGINS: str = "http://localhost:3000"

    DATABASE_URL: str = "sqlite://:memory:"  # Default to in-memory SQLite database
    OPENAI_API_KEY: str = ""  # Empty by default but should be set via .env

    @field_validator("ALLOWED_ORIGINS", mode="before")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
