from typing import Optional

from pydantic import BaseModel


class LevelReportBase(BaseModel):
    title: Optional[str]


class UpdateLevelReport(LevelReportBase):
    status: Optional[str]


class CreateLevelReport(LevelReportBase):
    status: str
    user_id: int


class CreateMyLevelReport(LevelReportBase):
    status: str


class LevelReport(LevelReportBase):
    id: int
    status: str
    user_id: int

    class Config:
        orm_mode = True
