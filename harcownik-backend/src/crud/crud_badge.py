from sqlalchemy.orm import Session

from src.models.badge import Badge as BadgeModel
from src.schemas.badge import Badge, CreateBadge, BadgeBase

def get_badge(db: Session, badge_id: int):
    return db.query(BadgeModel).filter(BadgeModel.id == badge_id).first()

def get_badges(db: Session):
    return db.query(BadgeModel).all()

def create_badge(db: Session, badge: CreateBadge):
    db_badge = BadgeModel(group = badge.group, name = badge.name, description = badge.description)
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge