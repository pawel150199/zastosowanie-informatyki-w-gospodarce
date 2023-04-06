from sqlalchemy.orm import Session
from . import models, schemas

# User
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.CreateUser, group_id: int, badge_id: int):
    db_user = models.User(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        level = user.level,
        function = user.function,
        group_id = group_id,
        badge_id = badge_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Badge
def get_badge(db: Session, badge_id: int):
    return db.query(models.Badge).filter(models.Badge.id == badge_id).first()

def create_badge(db: Session, badge: schemas.CreateBadge):
    db_badge = models.Badge(group = badge.group)
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge