from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.db import Base

class BadgeReport(Base):
    __tablename__ = 'badge_report'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    status = Column(String)
    badge_id = Column(Integer, ForeignKey("badge.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User")
    badge = relationship("Badge")