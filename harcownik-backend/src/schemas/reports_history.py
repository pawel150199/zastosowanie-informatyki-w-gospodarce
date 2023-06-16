from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PdfFileCreate(BaseModel):
    name: Optional[str]
    user_id: Optional[int]
    content: Optional[bytes]

    class Config:
        orm_mode = True


class PdfFile(BaseModel):
    id: Optional[int]
    name: Optional[str]
    user_id: Optional[int]

    class Config:
        orm_mode = True
