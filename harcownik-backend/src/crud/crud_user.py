from typing import Any, Dict, Optional, Union

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from src.core.security import get_password_hash, verify_password
from src.models.user import User as UserModel
from src.schemas.user import CreateScout, CreateUser, UpdateUser


# POST
def create_scout(db: Session, user: CreateScout, group_id: int) -> UserModel:
    db_user = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        is_teamadmin=False,
        is_webadmin=False,
        hashed_password=get_password_hash(user.password),
        level=user.level,
        function=user.function,
        group_id=group_id,
        badge_id=user.badge_id,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user(db: Session, user: CreateUser) -> UserModel:
    db_user = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        is_teamadmin=user.is_teamadmin,
        is_webadmin=user.is_webadmin,
        hashed_password=get_password_hash(user.password),
        level=user.level,
        function=user.function,
        group_id=user.group_id,
        badge_id=user.badge_id,
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


def get_users(db: Session) -> Optional[UserModel]:
    return db.query(UserModel).all()


def get_users_in_group(db: Session, group_id) -> Optional[UserModel]:
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
def delete_user(db: Session, user_id: int) -> Optional[UserModel]:
    db_user = db.query(UserModel).get(user_id)
    db.delete(db_user)
    db.commit()
    return db_user


# UPDATE
def update_user(
    db: Session, user_obj: UserModel, user_in: Union[UpdateUser, Dict[str, Any]]
) -> UserModel:
    obj_data = jsonable_encoder(user_obj)
    if isinstance(user_in, dict):
        update_data = user_in
    else:
        update_data = user_in.dict(exclude_unset=True)
    if update_data["password"]:
        hashed_password = get_password_hash(update_data["password"])
        del update_data["password"]
        update_data["hashed_password"] = hashed_password
    for field in obj_data:
        if field in update_data:
            setattr(user_obj, field, update_data[field])
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj
