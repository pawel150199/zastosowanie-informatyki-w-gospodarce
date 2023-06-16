from sqlalchemy import (Column, DateTime, ForeignKey, Integer, LargeBinary,
                        String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.db import Base


class PdfReport(Base):
    __tablename__ = "reports_history"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    content = Column(LargeBinary)
    user_id = Column(Integer, ForeignKey("user.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User")
