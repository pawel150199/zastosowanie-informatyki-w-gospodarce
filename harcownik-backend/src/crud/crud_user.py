from sqlalchemy.orm import Session

from src.models.user import User as UserModel
from src.schemas.user import User, CreateUser, UserBase

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_users(db: Session):
    return db.query(UserModel).all()

def create_user(db: Session, user: CreateUser):
    db_user = UserModel(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        level = user.level,
        function = user.function,
        group_id = user.group_id,
        badge_id = user.badge_id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user