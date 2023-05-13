from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None


class CreateUser(UserBase):
    level: str
    function: Optional[str]
    password: Optional[str]
    group_id: Optional[int]
    badge_id: Optional[int]
    is_teamadmin: bool = False
    is_webadmin: bool = False

class CreateScout(UserBase):
    level: str
    function: Optional[str]
    password: Optional[str]
    group_id: Optional[int]
    badge_id: Optional[int]

class User(UserBase):
    id: int
    level: str
    function: str
    group_id: int
    badge_id: int

    class Config:
        orm_mode = True

class UserWithId(User):
    id: int