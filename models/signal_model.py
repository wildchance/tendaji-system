from sqlalchemy import Column, Integer, String
from database.db import Base

class SignalLog(Base):
    __tablename__ = "signal_logs"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    action = Column(String, nullable=False)
    strength = Column(Integer, nullable=False)
