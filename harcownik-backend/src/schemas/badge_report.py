from pydantic import BaseModel
from typing import Optional

class BadgeReportBase(BaseModel):
    title: str

class UpdateBadgeReport(BadgeReportBase):
    status: Optional[str]

class CreateBadgeReport(BadgeReportBase):
    status: str
    user_id: int
    badge_id: int 

class BadgeReport(BadgeReportBase):
    status: str
    user_id: int
    badge_id: int

    class Config:
        orm_mode = True    