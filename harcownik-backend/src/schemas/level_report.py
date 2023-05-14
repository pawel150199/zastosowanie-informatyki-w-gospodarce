from pydantic import BaseModel
from typing import Optional

class LevelReportBase(BaseModel):
    title: Optional[str]


class UpdateLevelReport(LevelReportBase):
    status: Optional[str]

class CreateLevelReport(LevelReportBase):
    status: str
    user_id: int

class LevelReport(LevelReportBase):
    status: str
    user_id: int

    class Config:
        orm_mode = True