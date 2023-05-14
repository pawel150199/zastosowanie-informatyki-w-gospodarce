from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import Union, Dict, Any

from src.models.level_report import LevelReport as LevelReportModel
from src.models.user import User
from src.schemas.level_report import CreateLevelReport, UpdateLevelReport
from src.core.security import get_password_hash

# POST
def create_level_report(db:Session, level_report: CreateLevelReport, user_id: int):
    db_level_report = LevelReportModel(
        title=level_report.title,
        status=level_report.status,
        user_id=user_id
    )

    db.add(db_level_report)
    db.commit()
    db.refresh(db_level_report)
    return db_level_report

# GET
def get_level_report(db: Session, level_report_id: int):
    return db.query(LevelReportModel).filter(LevelReportModel.id == level_report_id).first()

def get_level_report_by_group(db: Session, group_id: int):
    return db.query(LevelReportModel).join(User).filter(User.group_id == group_id).all()


# DELETE
def delete_level_report(db: Session, level_report_id: int):
    db_level_report = db.query(LevelReportModel).get(level_report_id)
    db.delete(db_level_report)
    db.commit()
    return db_level_report 

# UPDATE
def update_level_report(db: Session, report_in: LevelReportModel, updated_report: Union[UpdateLevelReport, Dict[str, Any]]) -> LevelReportModel:
    obj_data = jsonable_encoder(report_in)
    if isinstance(updated_report, dict):
        update_data = updated_report
    else:
        update_data = updated_report.dict(exclude_unset=True)

    for field in obj_data:
            if field in update_data:
                setattr(report_in, field, update_data[field])
    db.add(report_in)
    db.commit()
    db.refresh(report_in)
    return report_in