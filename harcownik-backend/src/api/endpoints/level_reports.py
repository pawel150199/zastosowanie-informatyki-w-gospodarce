from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import get_db

router = APIRouter()

@router.post("/level_reports/", response_model=schemas.LevelReport)
def create_level_report(level_report: schemas.CreateLevelReport, db:Session = Depends(get_db)):
    return crud.create_level_report(db=db, level_report=level_report)

@router.get("/level_reports/", response_model=list[schemas.LevelReport])
def read_level_reports(db: Session = Depends(get_db)):
    level_reports = crud.get_level_reports(db)
    return level_reports

@router.get("/level_reports/{level_report_id}", response_model=schemas.LevelReport)
def read_level_report(level_report_id: int, db: Session = Depends(get_db)):
    db_level_report = crud.get_level_report(db=db, level_report_id=level_report_id)
    if db_level_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_level_report