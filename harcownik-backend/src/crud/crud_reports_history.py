from asyncio.log import logger
from sqlalchemy.orm import Session
from typing import Any, Dict, Union
from fastapi import File, UploadFile

from src.models.reports_history import PdfReport
from src.schemas.reports_history import PdfFile, PdfFileCreate

# POST
def create_file(db: Session, pdf_report: PdfFileCreate) -> PdfReport:
    db_pdf_report = PdfReport(
        name = pdf_report.name,
        user_id = pdf_report.user_id,
        content = pdf_report.content
    )
    db.add(db_pdf_report)
    db.commit()
    db.refresh(db_pdf_report)
    return db_pdf_report

# GET
def get_files(db: Session):
    return db.query(PdfReport).all()


def get_file(db: Session, pdf_id: int):
    return db.query(PdfReport).filter(PdfReport.id == pdf_id).first()


def get_files_by_user(db: Session, user_id: int):
    return db.query(PdfReport).filter(PdfReport.user_id == user_id).all()


# DELETE
def delete_file(db: Session, pdf_id: int):
    db_pdf = db.query(PdfReport).get(pdf_id)
    db.delete(db_pdf)
    db.commit()
    return db_pdf