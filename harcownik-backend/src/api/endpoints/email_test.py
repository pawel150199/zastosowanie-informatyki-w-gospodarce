from typing import Any
from fastapi import APIRouter
from src import schemas
from src.utils import send_test_email

router =  APIRouter()

@router.post("/test-email/", response_model=schemas.Message, status_code=201)
def test_email(email_to: str) -> Any:
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}