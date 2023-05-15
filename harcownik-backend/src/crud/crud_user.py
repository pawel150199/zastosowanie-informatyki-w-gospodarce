from fastapi import HTTPException
from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session

from src.models.user import User as UserModel
from src.schemas.user import  CreateUser
from src.core.security import get_password_hash, verify_password


# POST
def create_scout(db: Session, user: CreateUser, group_id) -> UserModel:
    db_user = UserModel(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        hashed_password = get_password_hash(user.password),
        level = user.level,
        function = user.function,
        group_id = group_id,
        badge_id = user.badge_id,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user(db: Session, user: CreateUser) -> UserModel:
    db_user = UserModel(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        is_teamadmin = user.is_teamadmin,
        is_webadmin = user.is_webadmin,
        hashed_password = get_password_hash(user.password),
        level = user.level,
        function = user.function,
        group_id = user.group_id,
        badge_id = user.badge_id,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# GET
def get_by_email(db: Session, email: str) -> Optional[UserModel]:
    return db.query(UserModel).filter(UserModel.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def authenticate(db: Session, email: str, password: str) -> Optional[UserModel]: 
    user = get_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=403, detail="no user")
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=403, detail="password not correct")
    return user
    
def get_users(db: Session):
    return db.query(UserModel).all()

def get_users_in_group(db: Session, group_id):
    return db.query(UserModel).filter(UserModel.group_id == group_id).all()

def is_teamadmin(user: UserModel) -> bool:
    return user.is_teamadmin

def is_webadmin(user: UserModel) -> bool:
    return user.is_webadmin

def is_webadmin_or_teamadmin(user: UserModel) -> bool:
    if user.is_teamadmin or user.is_webadmin:
        return True 
    else:
        return False

# DELETE
def delete_user(db: Session, user_id: int):
    db_user = db.query(UserModel).get(user_id)
    db.delete(db_user)
    db.commit()
    return db_user
