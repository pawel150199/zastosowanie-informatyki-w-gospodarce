from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, schemas
from src.api.helper import get_db

router = APIRouter()

# POST
@router.post("/badges/", response_model=schemas.Badge)
def create_badge(badge: schemas.CreateBadge, db:Session = Depends(get_db)):
    return crud.create_badge(db=db, badge=badge)

# GET
@router.get("/badges/", response_model=list[schemas.Badge])
def read_badges(db: Session = Depends(get_db)):
    badges = crud.get_badges(db)
    return badges

@router.get("/badges/grouped", response_model=list[schemas.BadgeAll])
def read_badges(db: Session = Depends(get_db)):
    groups = crud.get_badge_groups(db)
    result = []
    for group in groups:
        badges = crud.get_badges_by_group(db, str(group["group"]))
        one_group = {
            **group,
            "badges": [{"name": badge.name, "description": badge.description} for badge in badges],
        }
        result.append(one_group)
    
    return result


@router.get("/badges/groups", response_model=list[schemas.BadgeGroup])
def get_badge_groups(db: Session = Depends(get_db)):
    badge_groups = crud.get_badge_groups(db)
    return badge_groups

@router.get("/badges/group/{group}", response_model=list[schemas.BadgeBaseWithId])
def get_badges_by_group(group: str, db: Session = Depends(get_db)):
    badges = crud.get_badges_by_group(db, group=group)
    if badges is None:
        raise HTTPException(
            status_code=404,
            detail="Badges not found"
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
def delete_badge(badge_id: int, db: Session = Depends(get_db)):
    badge = crud.get_badge(db=db, badge_id=badge_id)
    if not badge:
        raise HTTPException(status_code=404, detail="Badge not found")
    badge = crud.delete_badge(db=db, badge_id=badge_id)
    return badge