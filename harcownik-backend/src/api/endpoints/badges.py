from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import get_db

router = APIRouter()

@router.post("/badges/", response_model=schemas.Badge)
def create_badge(badge: schemas.CreateBadge, db:Session = Depends(get_db)):
    return crud.create_badge(db=db, badge=badge)

@router.get("/badges/", response_model=list[schemas.Badge])
def read_groups(db: Session = Depends(get_db)):
    badges = crud.get_badges(db)
    return badges

@router.get("/badges/{badge_id}", response_model=schemas.Badge)
def read_badge(badge_id: int, db: Session = Depends(get_db)):
    db_badge = crud.get_badge(db, badge_id=badge_id)
    if db_badge is None:
        raise HTTPException(status_code=404, detail="Badge not found")
    return db_badge