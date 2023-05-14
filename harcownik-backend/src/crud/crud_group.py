from sqlalchemy.orm import Session
from typing import Dict, Union, Any
from fastapi.encoders import jsonable_encoder

from src.models.group import Group as GroupModel
from src.schemas.group import CreateGroup, UpdateGroup

# POST
def create_group(db:Session, group: CreateGroup):
    db_group = GroupModel(
        name=group.name,
        number=group.number,
        szczep=group.szczep,
        city=group.city
    )

    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

# GET
def get_group(db: Session, group_id: int):
    return db.query(GroupModel).filter(GroupModel.id == group_id).first()

def get_groups(db: Session):
    return db.query(GroupModel).all()

# DELETE
def delete_group(db: Session, group_id: int):
    db_group = db.query(GroupModel).get(group_id)
    db.delete(db_group)
    db.commit()
    return db_group

# UPDATE
def update_group(db: Session, group_in: GroupModel, updated_group: Union[UpdateGroup, Dict[str, Any]]) -> GroupModel:
    obj_data = jsonable_encoder(group_in)
    if isinstance(updated_group, dict):
        update_data = updated_group
    else:
        update_data = updated_group.dict(exclude_unset=True)

    for field in obj_data:
            if field in update_data:
                setattr(group_in, field, update_data[field])
    db.add(group_in)
    db.commit()
    db.refresh(group_in)
    return group_in