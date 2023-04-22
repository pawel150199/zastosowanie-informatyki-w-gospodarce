from pydantic import BaseModel

class BadgeBase(BaseModel):
    name: str
    description: str

class CreateBadge(BadgeBase):
    group: str

class Badge(BadgeBase):
    group: str
    
    class Config:
        orm_mode = True
