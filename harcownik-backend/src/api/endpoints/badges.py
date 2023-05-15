from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, schemas, models
from src.api.helper import get_db, get_current_teamadmin

router = APIRouter()

# POST
@router.post("/badges/", response_model=schemas.Badge)
def create_badge(badge: schemas.CreateBadge, db:Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)):
    return crud.create_badge(db=db, badge=badge)

# GET
@router.get("/badges/", response_model=list[schemas.Badge])
def read_badges(db: Session = Depends(get_db)):
    badges = crud.get_badges(db)
    if badges is None or badges == []:
        raise HTTPException(
            status_code=404,
            detail="Badges not found"
        )
    return badges

@router.get("/badges/grouped", response_model=list[schemas.BadgeAll])
def read_badges(db: Session = Depends(get_db)):
    groups = crud.get_badge_groups(db)
    if groups is None or groups == []:
        raise HTTPException(
            status_code=404,
            detail="Badge group not found"
        )
        
    result = []
    for group in groups:
        badges = crud.get_badges_by_group(db, str(group["group"]))
        if badges is None or badges == []:
            raise HTTPException(
                status_code=404,
                detail="Badges not found"
            )
        one_group = {
            **group,
            "badges": [{"name": badge.name, "description": badge.description} for badge in badges],
        }
        result.append(one_group)
    return result


@router.get("/badges/groups", response_model=list[schemas.BadgeGroup])
def get_badge_groups(db: Session = Depends(get_db)):
    badge_groups = crud.get_badge_groups(db)
    if badge_groups is None or badge_groups == []:
        raise HTTPException(
            status_code=404,
            detail="Badges groups not found"
        )
    return badge_groups

@router.get("/badges/group/{group}", response_model=list[schemas.BadgeBaseWithId])
def get_badges_by_group(group: str, db: Session = Depends(get_db)):
    badges = crud.get_badges_by_group(db, group=group)
    if badges is None:
        raise HTTPException(
            status_code=404,
            detail="Badge group not found"
        )
    return badges

@router.get("/badges/{badge_id}", response_model=schemas.Badge)
def read_badge(badge_id: int, db: Session = Depends(get_db)):
    badges = crud.get_badge(db, badge_id=badge_id)
    if badges is None:
        raise HTTPException(
            status_code=404,
            detail="Badge not found"
        )
    return badges

# DELETE
@router.delete("/badge/delete/{badge_id}", response_model=schemas.Badge)
def delete_badge(badge_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)):
    badge = crud.get_badge(db=db, badge_id=badge_id)
    if not badge:
        raise HTTPException(
            status_code=404,
            detail="Badge not found"
        )
    badge = crud.delete_badge(db=db, badge_id=badge_id)
    return badge