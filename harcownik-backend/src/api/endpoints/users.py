from typing import Any
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.utils import send_new_account_email
from src.core.settings import settings
from src.api.helper import get_db, get_current_user, get_current_teamadmin, get_current_webadmin, get_current_webadmin_or_teamadmin

router = APIRouter()

# POST
@router.post("/users/scout", response_model=schemas.User)
def create_scout(user: schemas.CreateScout, db: Session = Depends(get_db), current_teamadmin: models.User = Depends(get_current_teamadmin)) -> Any:
    db_user = crud.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exist in the system"
        )
    if settings.EMAILS_ENABLED and user.email:
        send_new_account_email(
            email_to=user.email, username=user.first_name, password=user.password
        )
    return crud.create_scout(db=db, user=user, group_id=current_teamadmin.group_id)

@router.post("/users/admin", response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db), _: models.User = Depends(get_current_webadmin)) -> Any:
    db_user = crud.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=401,
            detail="The user with this username already exist in the system"
        )
    if settings.EMAILS_ENABLED and user.email:
        send_new_account_email(
            email_to=user.email, username=user.first_name, password=user.password
        )
    return crud.create_user(db=db, user=user)

# GET
@router.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db), _: models.User = Depends(get_current_webadmin_or_teamadmin)) -> Any:
    users = crud.get_users(db)
    if users == [] or users is None:
        raise HTTPException(
            status_code=404,
            detail="Users not found"
        )
    return users

@router.get("/users/group/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db),  current_user: models.User = Depends(get_current_user)) -> Any:
    users = crud.get_users_in_group(db, group_id=current_user.group_id)
    if users == [] or users is None:
        raise HTTPException(
            status_code=404,
            detail="Users not found"
        )
    return users

@router.get("/me", response_model=schemas.UserWithId)
def read_user_me(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)) -> Any:
    if current_user is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized! Please login"
        )
    return current_user
    
@router.get("/users/id/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_webadmin_or_teamadmin)) -> Any:
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
       raise HTTPException(
           status_code=404,
           detail="User not found"
        )
    return db_user

@router.get("/users/email/{email}", response_model=schemas.User)
def get_user_by_email(email: str, db: Session = Depends(get_db), _: models.User = Depends(get_current_webadmin_or_teamadmin)) -> Any:
    db_user = crud.get_by_email(db, email=email)
    if db_user is None:
       raise HTTPException(
           status_code=404,
           detail="User not found"
           )
    return db_user

# DELETE
@router.delete("/user/delete/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_webadmin)) -> Any:
    user = crud.get_user(db=db,user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    user = crud.delete_user(db=db, user_id=user_id)
    return user

@router.delete("/user/group/delete/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_teamadmin)) -> Any:
    user = crud.get_user(db=db,user_id=user_id)
    if user.group_id != current_user.group_id:
        raise HTTPException(
            status_code=401,
            detail="Not enough privileges"
        )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    user = crud.delete_user(db=db, user_id=user_id)
    return user

# UPDATE
@router.put("/user/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_in: schemas.UpdateUser, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_webadmin_or_teamadmin)) -> Any:
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
    )
    user = crud.update_user(db, user_obj=user, user_in=user_in)
    return user
