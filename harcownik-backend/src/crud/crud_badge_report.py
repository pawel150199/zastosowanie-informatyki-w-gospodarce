from sqlalchemy.orm import Session

from src.models.badge_report import BadgeReport as BadgeReportModel
from src.schemas.badge_report import CreateBadgeReport

# POST
def create_badge_report(db: Session, badge_report: CreateBadgeReport, user_id):
    db_badge_report = BadgeReportModel(
        title=badge_report.title,
        status=badge_report.status,
        user_id=user_id,
        badge_id=badge_report.badge_id
    )

    db.add(db_badge_report)
    db.commit()
    db.refresh(db_badge_report)
    return db_badge_report

# GET
def get_badge_report(db: Session, badge_report_id: int):
    return db.query(BadgeReportModel).filter(BadgeReportModel.id == badge_report_id).first()

def get_badge_report_by_user(db: Session, user_id: int):
    return  db.query(BadgeReportModel).filter(BadgeReportModel.user_id == user_id).all()

def get_badge_report_by_badge(db: Session, badge_id: int):
    return  db.query(BadgeReportModel).filter(BadgeReportModel.badge_id == badge_id).all()

def get_badge_reports(db: Session):
    return db.query(BadgeReportModel).all()

# DELETE
def delete_badge_report(db: Session, badge_report_id: int):
    db_badge_report = db.query(BadgeReportModel).get(badge_report_id)
    db.delete(db_badge_report)
    db.commit()
    return db_badge_report