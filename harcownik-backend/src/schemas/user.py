from pydantic import BaseModel
from typing import Optional, Union

class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None
    is_teamadmin: bool = False
    is_webadmin: bool = False

class CreateUser(UserBase):
    level: str
    function: Optional[str]
    password: Optional[str]
    group_id: Optional[int]
    badge_id: Optional[int]

class User(UserBase):
    id: int
    level: Optional[str]
    function: Optional[str]
    group_id: Optional[int]
    badge_id: Optional[int]

    class Config:
        orm_mode = True

class UserWithId(User):
    id: int