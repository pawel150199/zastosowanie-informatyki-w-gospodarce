from typing import Any, Dict, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from src.models.badge_report import BadgeReport as BadgeReportModel
from src.models.user import User
from src.schemas.badge_report import CreateBadgeReport, UpdateBadgeReport


# POST
def create_badge_report(db: Session, badge_report: CreateBadgeReport, user_id: int):
    db_badge_report = BadgeReportModel(
        title=badge_report.title,
        status=badge_report.status,
        user_id=user_id,
        badge_id=badge_report.badge_id,
    )

    db.add(db_badge_report)
    db.commit()
    db.refresh(db_badge_report)
    return db_badge_report


# GET
def get_badge_report(db: Session, badge_report_id: int):
    return (
        db.query(BadgeReportModel)
        .filter(BadgeReportModel.id == badge_report_id)
        .first()
    )


def get_badge_report_by_user(db: Session, user_id: int):
    return db.query(BadgeReportModel).filter(BadgeReportModel.user_id == user_id).all()


def get_badge_report_by_group(db: Session, group_id: int):
    return db.query(BadgeReportModel).join(User).filter(User.group_id == group_id).all()


def get_badge_report_by_badge(db: Session, badge_id: int):
    return db.query(BadgeReportModel).filter(BadgeReportModel.id == badge_id ).all()


# DELETE
def delete_badge_report(db: Session, badge_report_id: int):
    db_badge_report = db.query(BadgeReportModel).get(badge_report_id)
    db.delete(db_badge_report)
    db.commit()
    return db_badge_report


# UPDATE
def update_badge_report(
    db: Session,
    report_obj: BadgeReportModel,
    report_in: Union[UpdateBadgeReport, Dict[str, Any]],
) -> BadgeReportModel:
    obj_data = jsonable_encoder(report_obj)
    if isinstance(report_in, dict):
        update_data = report_in
    else:
        update_data = report_in.dict(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(report_obj, field, update_data[field])
    db.add(report_obj)
    db.commit()
    db.refresh(report_obj)
    return report_obj
