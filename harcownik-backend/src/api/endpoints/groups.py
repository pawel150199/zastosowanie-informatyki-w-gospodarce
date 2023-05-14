from fastapi import Depends, HTTPException, APIRouter
from typing import Any
from sqlalchemy.orm import Session
from src import crud, schemas, models
from src.api.helper import get_db, get_current_teamadmin, get_current_webadmin_or_teamadmin

router = APIRouter()

# POST
@router.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.CreateGroup, db:Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)) -> Any:
    return crud.create_group(db=db, group=group)

# GET
@router.get("/groups/", response_model=list[schemas.Group])
def read_groups(db: Session = Depends(get_db)) -> Any:
    groups = crud.get_groups(db)
    if groups is None or groups == []:
        raise HTTPException(
            status_code=404,
            detail="Groups not found"
        )
    return groups

@router.get("/groups/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)) -> Any:
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(
            status_code=404,
            detail="Group not found"
        )
    return db_group

# DELETE
@router.delete("/group/delete/{group_id}", response_model=schemas.Group)
def delete_group(group_id: int, db: Session = Depends(get_db), _: models.User = Depends(get_current_teamadmin)) -> Any:
    group = crud.get_group(db=db, group_id=group_id)
    if not group:
        raise HTTPException(
            status_code=404,
            detail="Group not found"
        )
    group = crud.delete_group(db=db, group_id=group_id)
    return group

# UPDATE
@router.put("/group_report/{group_id}", response_model=schemas.Group)
def update_group(group_id: int, group_in: schemas.UpdateGroup, db: Session = Depends(get_db), _: models.Group = Depends(get_current_webadmin_or_teamadmin)) -> Any:
    group = crud.get_group(db, group_id=group_id)
    if not group:
        raise HTTPException(
            status_code=404,
            detail="The group with this username does not exist in the system",
    )
    level_report = crud.update_group(db, group_obj=group, group_in=group_in)
    return level_report