from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import (get_current_teamadmin, get_current_user,
                            get_current_webadmin,
                            get_current_webadmin_or_teamadmin, get_db)

router = APIRouter()


# POST
@router.post("/me/badge_reports/", response_model=schemas.BadgeReport)
def create_badge_report(
    badge_report: schemas.CreateMyBadgeReport,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
) -> Any:
    badge_report_in = crud.get_badge_report_by_user(db, user_id=current_user.id)
    if any(
        badge_report.title == report.title and badge_report.status == report.status
        for report in badge_report_in
    ):
        raise HTTPException(status_code=400, detail="Similar report exist")
    return crud.create_badge_report(
        db=db, badge_report=badge_report, user_id=current_user.id
    )


# GET
# @router.get("/badge_reports/", response_model=list[schemas.BadgeReport])
# def read_badge_reports(db: Session = Depends(get_db), _: models.User = Depends(get_current_webadmin)):
#    badge_reports = crud.get_badge_reports(db)
#    if badge_reports is None or badge_reports == []:
#        raise HTTPException(
#            status_code=404,
#            detail="Badge reports not found"
#        )
#    return badge_reports


@router.get("/group/badge_reports/", response_model=list[schemas.BadgeReport])
def read_badge_reports_in_my_group(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_teamadmin),
) -> Any:
    badge_reports = crud.get_badge_report_by_group(db, group_id=current_user.group_id)
    if badge_reports is None or badge_reports == []:
        raise HTTPException(status_code=404, detail="Badge reports not found")
    return badge_reports


@router.get("/me/badge_reports", response_model=list[schemas.BadgeReport])
def read_my_badges_reports(
    db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
) -> Any:
    me = current_user.id
    db_badge_report = crud.get_badge_report_by_user(db, user_id=me)
    if db_badge_report is None or db_badge_report == []:
        raise HTTPException(status_code=404, detail="Badge reports not found")
    return db_badge_report


@router.get("/badge_reports/badge/{badge_id}", response_model=list[schemas.BadgeReport])
def read_badges_reports_by_badge(badge_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)):
    db_badge_report = crud.get_badge_report(db, badge_id=badge_id)
    if db_badge_report is None:
        raise HTTPException(
            status_code=404,
            detail="Badge report not found"
        )
    return db_badge_report


# DELETE
@router.delete(
    "/badge_report/delete/{badge_report_id}", response_model=schemas.BadgeReport
)
def delete_badge_report(
    badge_report_id: int,
    db: Session = Depends(get_db),
    _: models.User = Depends(get_current_webadmin),
) -> Any:
    badge_report = crud.get_badge_report(db=db, badge_report_id=badge_report_id)
    if not badge_report:
        raise HTTPException(status_code=404, detail="Badge report not found")
    badge_report = crud.delete_badge_report(db=db, badge_report_id=badge_report_id)
    return badge_report


# UPDATE
@router.put("/badge_report/{badge_report_id}", response_model=schemas.BadgeReport)
def update_badge_report(
    badge_report_id: int,
    level_report_in: schemas.UpdateBadgeReport,
    db: Session = Depends(get_db),
    _: models.BadgeReport = Depends(get_current_webadmin_or_teamadmin),
) -> Any:
    level_report = crud.get_badge_report(db, badge_report_id=badge_report_id)
    if not level_report:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    level_report = crud.update_badge_report(
        db, report_obj=level_report, report_in=level_report_in
    )
    return level_report
