import secrets
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PROJECT_NAME: str = "Harcownik"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "172.18.0.3"
    ALGORITHM: str = "HS256"
    SERVER_HOST: AnyHttpUrl = "http://172.18.0.3:8000"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://172.18.0.4:80"]

    # DATABASE
    POSTGRES_SERVER: str = "172.18.0.2"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "postgres"
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