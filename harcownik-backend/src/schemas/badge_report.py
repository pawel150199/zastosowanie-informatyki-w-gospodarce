from typing import Optional

from pydantic import BaseModel


class BadgeReportBase(BaseModel):
    title: str


class UpdateBadgeReport(BadgeReportBase):
    status: Optional[str]


class CreateBadgeReport(BadgeReportBase):
    status: str
    user_id: int
    badge_id: int


class CreateMyBadgeReport(BadgeReportBase):
    status: str
    badge_id: int


class BadgeReport(BadgeReportBase):
    status: str
    user_id: int
    badge_id: int

    class Config:
        orm_mode = True
