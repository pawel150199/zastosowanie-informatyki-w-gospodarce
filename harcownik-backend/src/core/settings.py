import secrets
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PROJECT_NAME: str = "Harcownik"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "localhost"
    ALGORITHM: str = "HS256"
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    # DATABASE
    POSTGRES_SERVER: str = None
    POSTGRES_USER: str = None
    POSTGRES_PASSWORD: str = None
    POSTGRES_DB: str = None
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    # SMTP
    SMTP_PORT: Optional[int] = 465
    SMTP_HOST: Optional[str] = "smtp.gmail.com"
    SMTP_USER: Optional[str] = "harcownikapp@gmail.com"
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = "harcownikapp@gmail.com"
    EMAILS_FROM_NAME: Optional[str] = "Harcownik"

    # EMAIL
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAILS_ENABLED: bool = False
    EMAIL_TEST_USER: str = None


settings = Settings()