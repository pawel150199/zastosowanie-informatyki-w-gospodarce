from typing import Optional, List
from src.schemas.badge import Badge
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None


class CreateUser(UserBase):
    level: str
    function: Optional[str]
    password: Optional[str]
    group_id: Optional[int]
    is_teamadmin: bool = False
    is_webadmin: bool = False
    badge_ids: Optional[list[int]] = []



class CreateScout(UserBase):
    level: str
    function: Optional[str]
    password: Optional[str]
    group_id: Optional[int]
    badge_ids: Optional[list[int]] = []


class UpdateUser(UserBase):
    level: Optional[str]
    password: Optional[str]
    function: Optional[str]
    group_id: Optional[int]
    badge_ids: Optional[list[int]] = []


class User(UserBase):
    id: int
    level: str
    function: str
    group_id: Optional[int]
    is_teamadmin: bool
    is_webadmin: bool
    badges: Optional[list[Badge]] = []

    class Config:
        orm_mode = True


class UserWithId(User):
    id: int
