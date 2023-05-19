from typing import Optional

from pydantic import BaseModel


class GroupBase(BaseModel):
    name: Optional[str]
    number: Optional[int]


class CreateGroup(GroupBase):
    szczep: str
    city: str


class UpdateGroup(GroupBase):
    szczep: Optional[str]
    city: Optional[str]


class Group(GroupBase):
    id: int
    szczep: str
    city: str

    class Config:
        orm_mode = True
