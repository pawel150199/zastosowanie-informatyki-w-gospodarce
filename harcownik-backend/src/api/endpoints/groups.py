from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, models, schemas
from src.api.helper import get_db

router = APIRouter()

@router.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.CreateGroup, db:Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)

@router.get("/groups/", response_model=list[schemas.Group])
def read_groups(db: Session = Depends(get_db)):
    groups = crud.get_groups(db)
    return groups

@router.get("/groups/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group