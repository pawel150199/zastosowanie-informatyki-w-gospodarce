from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db import Base

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(Integer)
    szczep = Column(String)
    city = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

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

class Badge(Base):
    __tablename__ = "badge"
    id = Column(Integer, primary_key=True)
    group = Column(String)
    name = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

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

class LevelReport(Base):
    __tablename__ = "level_report"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User")
        