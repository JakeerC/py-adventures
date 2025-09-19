from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    """
    A configuration class for handling application settings.

    The Settings class provides a centralized way to manage application-wide configurations.
    It includes options for API routing, debugging, CORS settings, database connections,
    and OpenAI API integration.

    Attributes:
        API_PREFIX (str): The prefix for all API endpoints.
        DEBUG (bool): A flag to enable or disable debug mode.
        ALLOWED_ORIGINS (str): Comma-separated string of allowed origins for CORS.
        DATABASE_URL (str): Connection URL for the database.
        OPENAI_API_KEY (str): API key for OpenAI integration (should be set via .env file).

    The class also includes validation for allowed origins and configuration for loading
    environment variables from a .env file with UTF-8 encoding.
    """

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
