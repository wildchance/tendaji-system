from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database.db import Base

class SignalLog(Base):
    __tablename__ = "signal_logs"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    action = Column(String, nullable=False)
    strength = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
