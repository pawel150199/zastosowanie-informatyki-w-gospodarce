from src.db.db import SessionLocal
from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt 
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.core import security
from src.db.db import SessionLocal
from src.core.settings import settings

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login/access_token")

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm=[settings.ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.get_user(db, user_id=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user
