from sqlalchemy.orm import Session

from src.models.level_report import LevelReport as LevelReportModel
from src.schemas.level_report import LevelReport, CreateLevelReport, LevelReportBase

def create_level_report(db:Session, level_report: CreateLevelReport):
    db_level_report = LevelReportModel(
        title=level_report.title,
        status=level_report.status,
        user_id=level_report.user_id
    )

    db.add(db_level_report)
    db.commit()
    db.refresh(db_level_report)
    return db_level_report

def get_level_report(db: Session, level_report_id: int):
    return db.query(LevelReportModel).filter(LevelReportModel.id == level_report_id).first()

def get_level_reports(db: Session):
    return db.query(LevelReportModel).all()