from xmlrpc.client import Boolean
from sqlalchemy import DateTime, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.db import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False, index=True)
    level = Column(String, nullable=True, index=True)
    function = Column(String, nullable=True, index=True)
    is_superuser = Column(Boolean(), default=False, index=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    badge_id = Column(Integer, ForeignKey("badge.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    group = relationship("Group")
    badge = relationship("Badge")