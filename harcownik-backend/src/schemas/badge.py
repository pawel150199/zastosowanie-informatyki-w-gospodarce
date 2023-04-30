from pydantic import BaseModel

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