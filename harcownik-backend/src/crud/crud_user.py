from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session

from src.models.user import User as UserModel
from src.schemas.user import User, CreateUser, UserBase
from src.core.security import get_password_hash, verify_password

# POST
def create_user(db: Session, user: CreateUser) -> UserModel:
    db_user = UserModel(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
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
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
    
def get_users(db: Session):
    return db.query(UserModel).all()

# DELETE
def delete_user(db: Session, user_id: int):
    db_user = db.query(UserModel).get(user_id)
    db.delete(db_user)
    db.commit()
    return db_user