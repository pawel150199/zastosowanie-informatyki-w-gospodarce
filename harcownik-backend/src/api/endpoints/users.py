from tokenize import Token
from typing import Any
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import get_db, get_current_user

router = APIRouter()

# POST
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exist in the system"
        )
    return crud.create_user(db=db, user=user)

# GET
@router.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@router.get("/me", response_model=schemas.User)
def read_user_me(db: Session = Depends(get_db),  current_user: models.User = Depends(get_current_user)) -> Any:
    return current_user
    
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
       raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/email/{email}", response_model=schemas.User)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_by_email(db, email=email)
    if db_user is None:
       raise HTTPException(status_code=404, detail="User not found")
    return db_user

# DELETE
@router.delete("/user/delete/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db,user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.delete_user(db=db, user_id=user_id)
    return user