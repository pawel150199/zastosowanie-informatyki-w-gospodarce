from sqlalchemy import JSON, Column, DateTime, Integer, String
from sqlalchemy.sql import func
from src.db.db import Base


class Badge(Base):
    __tablename__ = "badge"
    id = Column(Integer, primary_key=True, index=True)
    group = Column(String, index=True)
    name = Column(String, index=True)
    description = Column(JSON)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
