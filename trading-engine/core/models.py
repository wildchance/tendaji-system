from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TradeLog(Base):
    __tablename__ = "trade_logs"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    action = Column(String)
    price = Column(Float)
    volume = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    comment = Column(Text, nullable=True)
