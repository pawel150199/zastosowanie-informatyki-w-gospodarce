from pydantic import BaseModel

# Base models
class GroupBase(BaseModel):
    name: str
    number: str

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class BadgeBase(BaseModel):
    name: str

class BadgeReportBase(BaseModel):
    title: str

class LevelReportBase(BaseModel):
    title: str

# Create
class CreateGroup(BaseModel):
    szczep: str
    city: str

class CreateUser(UserBase):
    level: str
    function: str
    group_id: int
    badge_id: int

class CreateBadge(BadgeBase):
    group: str

class CreateBadgeReport(BadgeReportBase):
    status: str
    user_id: int
    badge_id: int 

class CreateLevelReport(LevelReportBase):
    status: str
    user_id: int

# Get
class Group(BaseModel):
    szczep: str
    city: str

    class Config:
        orm_mode = True

class User(UserBase):
    level: str
    function: str
    group_id: int
    badge_id: int

    class Config:
        orm_mode = True

class Badge(BadgeBase):
    group: str
    
    class Config:
        orm_mode = True

class BadgeReport(BadgeReportBase):
    status: str
    user_id: int
    badge_id: int

    class Config:
        orm_mode = True

class LevelReport(LevelReportBase):
    status: str
    user_id: int

    class Config:
        orm_mode = True
    