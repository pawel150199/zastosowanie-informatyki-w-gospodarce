from pydantic import BaseModel

class GroupBase(BaseModel):
    name: str
    number: str

class CreateGroup(GroupBase):
    szczep: str
    city: str

class Group(GroupBase):
    szczep: str
    city: str

    class Config:
        orm_mode = True    
