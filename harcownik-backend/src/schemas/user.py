from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None
    is_superuser: bool = False

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
    group_id: Optional[int]
    badge_id: Optional[int]

    class Config:
        orm_mode = True

class UserWithId(User):
    id: int