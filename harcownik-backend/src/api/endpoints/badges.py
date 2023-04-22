from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, models, schemas
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

@router.get("/badges/groups", response_model=schemas.Badge)
def read_badge_groups(db: Session = Depends(get_db)):
    badges_groups = crud.get_badge_groups(db)
    return badges_groups

@router.get("/badges/{badge_id}", response_model=schemas.Badge)
def read_badge(badge_id: int, db: Session = Depends(get_db)):
    db_badge = crud.get_badge(db, badge_id=badge_id)
    if db_badge is None:
        raise HTTPException(status_code=404, detail="Badge not found")
    return db_badge

# DELETE
@router.delete("/badge/delete/{badge_id}", response_model=schemas.Badge)
def delete_badge(badge_id: int, db: Session = Depends(get_db)):
    badge = crud.get_badge(db=db, badge_id=badge_id)
    if not badge:
        raise HTTPException(status_code=404, detail="Badge not found")
    badge = crud.delete_badge(db=db, badge_id=badge_id)
    return badge
