from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.db import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    level = Column(String)
    function = Column(String)
    group_id = Column(Integer, ForeignKey("group.id"))
    badge_id = Column(Integer, ForeignKey("badge.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    group = relationship("Group")
    badge = relationship("Badge")