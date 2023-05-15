from pydantic import BaseModel

class LevelReportBase(BaseModel):
    title: str

class CreateLevelReport(LevelReportBase):
    status: str
    user_id: int

class LevelReport(LevelReportBase):
    id: int
    status: str
    user_id: int

    class Config:
        orm_mode = True