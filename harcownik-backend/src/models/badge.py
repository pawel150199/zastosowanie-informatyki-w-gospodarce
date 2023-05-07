from sqlalchemy import DateTime, Column, Integer, String
from sqlalchemy.sql import func
from src.db.db import Base

class Badge(Base):
    __tablename__ = "badge"
    id = Column(Integer, primary_key=True)
    group = Column(String)
    name = Column(String)
    description = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
