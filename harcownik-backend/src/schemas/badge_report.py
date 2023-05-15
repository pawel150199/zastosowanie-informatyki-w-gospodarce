from pydantic import BaseModel
from typing import Optional

class BadgeReportBase(BaseModel):
    title: str

class CreateBadgeReport(BadgeReportBase):
    status: str
    user_id: int
    badge_id: int 

class BadgeReport(BadgeReportBase):
    id: int
    status: str
    user_id: int
    badge_id: int

    class Config:
        orm_mode = True    