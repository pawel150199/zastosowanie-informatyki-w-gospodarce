from sqlalchemy.orm import Session

from src.models.badge import Badge as BadgeModel
from src.schemas.badge import Badge, CreateBadge, BadgeBase

# POST
def create_badge(db: Session, badge: CreateBadge):
    db_badge = BadgeModel(group = badge.group, name = badge.name, description = badge.description)
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge

# GET
def get_badge(db: Session, badge_id: int):
    return db.query(BadgeModel).filter(BadgeModel.id == badge_id).first()

def get_badge_groups(db: Session):
    return db.query(BadgeModel.group).order_by(BadgeModel.group.asc()).distinct().all()

def get_badges_by_group(db: Session, group: str):
    return db.query(BadgeModel).filter(BadgeModel.group == group).all()

def get_badges(db: Session):
    return db.query(BadgeModel).all()        

# DELETE
def delete_badge(db: Session, badge_id: int):
    db_badge = db.query(BadgeModel).get(badge_id)
    db.delete(db_badge)
    db.commit()
    return db_badge