from typing import Any
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import get_db
from src.utils import send_test_email

router =  APIRouter()

@router.post("/test-email/", response_model=schemas.Message, status_code=201)
def test_email(email_to: str) -> Any:
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}