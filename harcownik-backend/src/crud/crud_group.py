from sqlalchemy.orm import Session

from src.models.group import Group as GroupModel
from src.schemas.group import Group, CreateGroup, GroupBase

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