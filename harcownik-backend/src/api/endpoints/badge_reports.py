from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, schemas, models
from src.api.helper import get_db, get_current_user

router = APIRouter()

# POST
@router.post("/badge_reports/", response_model=schemas.BadgeReport)
def create_badge_report(badge_report: schemas.CreateBadgeReport, db:Session = Depends(get_db)):
    return crud.create_badge_report(db=db, badge_report=badge_report)

# GET
@router.get("/badge_reports/", response_model=list[schemas.BadgeReport])
def read_badge_reports(db: Session = Depends(get_db)):
    badge_reports = crud.get_badge_reports(db)
    if badge_reports is None or badge_reports == []:
        raise HTTPException(
            status_code=404,
            detail="Badge reports not found"
        )
    return badge_reports

@router.get("/badge_reports/{badge_report_id}", response_model=schemas.BadgeReport)
def read_group(badge_report_id: int, db: Session = Depends(get_db)):
    db_badge_report = crud.get_badge_report(db, badge_report_id=badge_report_id)
    if db_badge_report is None:
        raise HTTPException(
            status_code=404,
            detail="Badge report not found"
        )
    return db_badge_report

@router.get("/badge_reports/me/raports", response_model=schemas.BadgeReport)
def read_group(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    me = current_user.id
    db_badge_report = crud.get_badge_report(db, badge_report_id=me)
    if db_badge_report is None or db_badge_report == []:
        raise HTTPException(
            status_code=404,
            detail="Badge reports not found"
        )
    return db_badge_report

@router.get("/badge_reports/user/{user_id}", response_model=list[schemas.BadgeReport])
def read_group_by_user(user_id: int, db: Session = Depends(get_db)):
    db_badge_report = crud.get_badge_report_by_user(db, user_id=user_id)
    if db_badge_report is None:
        raise HTTPException(
            status_code=404,
            detail="Badge report not found"
        )
    return db_badge_report

@router.get("/badge_reports/badge/{badge_id}", response_model=list[schemas.BadgeReport])
def read_group_by_badge(badge_id: int, db: Session = Depends(get_db)):
    db_badge_report = crud.get_badge_report_by_badge(db, badge_id=badge_id)
    if db_badge_report is None:
        raise HTTPException(
            status_code=404,
            detail="Badge report not found"
        )
    return db_badge_report

# DELETE
@router.delete("/badge_report/delete/{badge_report_id}", response_model=schemas.BadgeReport)
def delete_badge_report(badge_report_id: int, db: Session = Depends(get_db)):
    badge_report = crud.get_badge_report(db=db, badge_report_id=badge_report_id)
    if not badge_report:
        raise HTTPException(
            status_code=404,
            detail="Badge report not found"
        )
    badge_report = crud.delete_badge_report(db=db, badge_report_id=badge_report_id)
    return badge_report