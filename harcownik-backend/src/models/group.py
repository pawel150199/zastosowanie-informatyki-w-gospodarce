from sqlalchemy import DateTime, Column, Integer, String
from sqlalchemy.sql import func
from src.db.db import Base

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    number = Column(Integer, index=True)
    szczep = Column(String, index=True)
    city = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())