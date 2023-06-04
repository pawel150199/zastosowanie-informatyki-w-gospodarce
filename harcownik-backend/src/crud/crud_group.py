from typing import Any, Dict, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from src.models.group import Group as GroupModel
from src.schemas.group import CreateGroup, UpdateGroup


# POST
def create_group(db: Session, group: CreateGroup):
    db_group = GroupModel(
        name=group.name, number=group.number, szczep=group.szczep, city=group.city
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


def get_group_by_number(db: Session, number: int):
    return db.query(GroupModel).filter(GroupModel.number == number).all()


# DELETE
def delete_group(db: Session, group_id: int):
    db_group = db.query(GroupModel).get(group_id)
    db.delete(db_group)
    db.commit()
    return db_group


# UPDATE
def update_group(
    db: Session, group_obj: GroupModel, group_in: Union[UpdateGroup, Dict[str, Any]]
) -> GroupModel:
    obj_data = jsonable_encoder(group_obj)
    if isinstance(group_in, dict):
        update_data = group_in
    else:
        update_data = group_in.dict(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(group_obj, field, update_data[field])
    db.add(group_obj)
    db.commit()
    db.refresh(group_obj)
    return group_obj
