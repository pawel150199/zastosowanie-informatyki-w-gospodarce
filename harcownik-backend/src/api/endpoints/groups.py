from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src import crud, schemas, models
from src.api.helper import get_db, get_current_teamadmin

router = APIRouter()

# POST
@router.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.CreateGroup, db:Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)):
    return crud.create_group(db=db, group=group)

# GET
@router.get("/groups/", response_model=list[schemas.Group])
def read_groups(db: Session = Depends(get_db)):
    groups = crud.get_groups(db)
    if groups is None or groups == []:
        raise HTTPException(
            status_code=404,
            detail="Groups not found"
        )
    return groups

@router.get("/groups/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(
            status_code=404,
            detail="Group not found"
        )
    return db_group

# DELETE
@router.delete("/group/delete/{group_id}", response_model=schemas.Group)
def delete_group(group_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)):
    group = crud.get_group(db=db, group_id=group_id)
    if not group:
        raise HTTPException(
            status_code=404,
            detail="Group not found"
        )
    group = crud.delete_group(db=db, group_id=group_id)
    return group