from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import get_db

router = APIRouter()

# POST
@router.post("/badge_reports/", response_model=schemas.BadgeReport)
def create_badge_report(badge_report: schemas.CreateBadgeReport, db:Session = Depends(get_db)):
    return crud.create_badge_report(db=db, badge_report=badge_report)

# GET
@router.get("/badge_reports/", response_model=list[schemas.BadgeReport])
def read_badge_reports(db: Session = Depends(get_db)):
    badge_reports = crud.get_badge_reports(db)
    return badge_reports

@router.get("/badge_reports/{badge_report_id}", response_model=schemas.BadgeReport)
def read_group(badge_report_id: int, db: Session = Depends(get_db)):
    db_badge_report = crud.get_badge_report(db, badge_report_id=badge_report_id)
    if db_badge_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_badge_report

# DELETE
@router.delete("/badge_report/delete/{badge_report_id}", response_model=schemas.BadgeReport)
def delete_badge_report(badge_report_id: int, db: Session = Depends(get_db)):
    badge_report = crud.get_badge_report(db=db, badge_report_id=badge_report_id)
    if not badge_report:
        raise HTTPException(status_code=404, detail="Badge Raport not found")
    badge_report = crud.delete_badge_report(db=db, badge_report_id=badge_report_id)
    return badge_report
