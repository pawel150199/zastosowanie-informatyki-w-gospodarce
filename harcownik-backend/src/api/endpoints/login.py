from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import get_current_user, get_db
from src.core import security
from src.core.security import get_password_hash
from src.core.settings import settings
from src.utils import (generate_password_reset_token,
                       send_reset_password_email, send_test_email,
                       verify_password_reset_token)

router = APIRouter()

# POST
@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = crud.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.email, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/test-email/", response_model=schemas.Message, status_code=201)
def test_email(email_to: str) -> Any:
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}


@router.post("/password-recovery/{email}", response_model=schemas.Message)
def recover_password(
    email: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
) -> Any:
    user = current_user
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}


@router.post("/reset-password", response_model=schemas.Message)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
) -> Any:
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")

    user = current_user
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}
