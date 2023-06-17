from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.db import Base

user_badges = Table(
    "user_badges",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("badge_id", Integer, ForeignKey("badge.id")),
)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False, index=True)
    level = Column(String, nullable=True, index=True)
    function = Column(String, nullable=False, index=True)
    is_teamadmin = Column(Boolean(), default=False, index=True)
    is_webadmin = Column(Boolean(), default=False, index=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    badges = relationship("Badge", secondary=user_badges, backref="users")
    group = relationship("Group")
    badge_report = relationship("BadgeReport", back_populates="user", cascade="all, delete")
    level_report = relationship("LevelReport", back_populates="user", cascade="all, delete")
