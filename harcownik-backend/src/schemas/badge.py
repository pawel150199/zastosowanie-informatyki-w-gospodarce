from pydantic import BaseModel
from typing import List

class BadgeGroup(BaseModel):
    group: str

class BadgeBase(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True

class CreateBadge(BadgeBase):
    group: str

class Badge(BadgeBase):
    group: str
    
    class Config:
        orm_mode = True

class BadgeAll(BaseModel):
    group: str
    badges: List[BadgeBase]

    class Config:
        orm_mode = True