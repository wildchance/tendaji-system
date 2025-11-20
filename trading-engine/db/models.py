from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class TradeJournal(Base):
    __tablename__ = "trade_journal"
    
    id = Column(Integer, primary_key=True, index=True)
    signal = Column(String, index=True)
    action = Column(String)
    price = Column(Float)
    status = Column(String, default="pending")
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
