from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class CreateUser(UserBase):
    level: str
    function: str
    password: str
    group_id: int
    badge_id: int

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