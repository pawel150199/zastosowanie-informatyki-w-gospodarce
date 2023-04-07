from pydoc import describe
from sqlalchemy.orm import Session
from . import models, schemas

# User
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(
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


# Badge
def get_badge(db: Session, badge_id: int):
    return db.query(models.Badge).filter(models.Badge.id == badge_id).first()

def get_badges(db: Session):
    return db.query(models.Badge).all()

def create_badge(db: Session, badge: schemas.CreateBadge):
    db_badge = models.Badge(group = badge.group, name = badge.name, description = badge.description)
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge

# Group
def create_group(db:Session, group: schemas.CreateGroup):
    db_group = models.Group(
        name=group.name,
        number=group.number,
        szczep=group.szczep,
        city=group.city
    )

    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

def get_groups(db: Session):
    return db.query(models.Group).all()

# BadgeReport
def create_badge_report(db:Session, badge_report: schemas.CreateBadgeReport):
    db_badge_report = models.BadgeReport(
        title=badge_report.title,
        status=badge_report.status,
        user_id=badge_report.user_id,
        badge_id=badge_report.badge_id
    )

    db.add(db_badge_report)
    db.commit()
    db.refresh(db_badge_report)
    return db_badge_report

def get_badge_report(db: Session, badge_report_id: int):
    return db.query(models.BadgeReport).filter(models.BadgeReport.id == badge_report_id).first()

def get_badge_reports(db: Session):
    return db.query(models.BadgeReport).all()

# LevelReport
def create_level_report(db:Session, level_report: schemas.CreateLevelReport):
    db_level_report = models.LevelReport(
        title=level_report.title,
        status=level_report.status,
        user_id=level_report.user_id
    )

    db.add(db_level_report)
    db.commit()
    db.refresh(db_level_report)
    return db_level_report

def get_level_report(db: Session, level_report_id: int):
    return db.query(models.LevelReport).filter(models.LevelReport.id == level_report_id).first()

def get_level_reports(db: Session):
    return db.query(models.LevelReport).all()