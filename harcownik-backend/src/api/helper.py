from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.core.settings import settings
from src.db.db import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login/access-token")


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.get_by_email(db, email=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_teamadmin(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.is_teamadmin(current_user):
        raise HTTPException(
            status_code=401, detail="The user doesn't have enough privileges"
        )
    return current_user


def get_current_webadmin(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.is_webadmin(current_user):
        raise HTTPException(
            status_code=401, detail="The user doesn't have enough privileges"
        )
    return current_user


def get_current_webadmin_or_teamadmin(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.is_webadmin_or_teamadmin(current_user):
        raise HTTPException(
            status_code=401, detail="The user doesn't have enough privileges"
        )
    return current_user
