from fastapi import Depends, HTTPException, APIRouter
from typing import Any
from sqlalchemy.orm import Session
from src import crud, schemas, models
from src.api.helper import get_db, get_current_user, get_current_webadmin, get_current_teamadmin, get_current_webadmin_or_teamadmin

router = APIRouter()

# POST
@router.post("/me/level_reports/", response_model=schemas.LevelReport)
def create_level_report(level_report: schemas.CreateLevelReport, db:Session = Depends(get_db), current_user: models.User = Depends(get_current_user)) -> Any:
    return crud.create_level_report(db=db, level_report=level_report, user_id=current_user.id)

# GET
@router.get("/group/level_reports/", response_model=list[schemas.LevelReport])
def read_level_reports_in_my_group(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_teamadmin)) -> Any:
    level_reports = crud.get_level_report_by_group(db, group_id=current_user.group_id)
    if level_reports is None or level_reports == []:
        raise HTTPException(
            status_code=404,
            detail="Badge reports not found"
        )
    return level_reports

#@router.get("/level_reports/", response_model=list[schemas.LevelReport])
#def read_level_reports(db: Session = Depends(get_db)):
#    level_reports = crud.get_level_reports(db)
#    if level_reports == [] or level_reports is None:
#        raise HTTPException(
#            status_code=404,
#            detail="Level reports not found"
#        )
#    return level_reports

#@router.get("/level_reports/{level_report_id}", response_model=schemas.LevelReport)
#def read_level_report(level_report_id: int, db: Session = Depends(get_db)):
#    db_level_report = crud.get_level_report(db=db, level_report_id=level_report_id)
#    if db_level_report is None:
#        raise HTTPException(
#            status_code=404,
#            detail="Report not found"
#        )
#    return db_level_report

@router.get("/level_reports/me/raports", response_model=list[schemas.LevelReport])
def read_level_report_by_user(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)) -> Any:
    me = current_user.id
    db_level_report = crud.get_level_report_by_user(db=db, user_id=me)
    if db_level_report is None or db_level_report == []:
        raise HTTPException(
            status_code=404,
            detail="Level reports not found"
        )
    return db_level_report

#@router.get("/level_reports/user/{user_id}", response_model=list[schemas.LevelReport])
#def read_level_report_by_user(user_id: int, db: Session = Depends(get_db)):
#    db_level_report = crud.get_level_report_by_user(db=db, user_id=user_id)
#    if db_level_report is None:
#        raise HTTPException(
#            status_code=404,
#            detail="Report not found"
#        )
#    return db_level_report

# DELETE
@router.delete("/level_report/delete/{level_report_id}", response_model=schemas.LevelReport)
def delete_level_report(level_report_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_webadmin)) -> Any:
    level_report = crud.get_level_report(db=db, level_report_id=level_report_id)
    if not level_report:
        raise HTTPException(
            status_code=404,
            detail="Level Raport not found"
        )
    level_report = crud.delete_level_report(db=db, level_report_id=level_report_id)
    return level_report


# UPDATE
@router.put("/{level_report_id}", response_model=schemas.LevelReport)
def update_level_report(level_report_id: int, level_report_in: schemas.UpdateLevelReport, db: Session = Depends(get_db), _: models.LevelReport = Depends(get_current_webadmin_or_teamadmin)) -> Any:
    level_report = crud.get_level_report(db, level_report_id=level_report_id)
    if not level_report:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
    )
    level_report = crud.update_level_report(db, report_in=level_report, updated_report = level_report_in)
    return level_report