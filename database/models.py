from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from .db import Base

class TradeLog(Base):
    __tablename__ = "trade_logs"

    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String, index=True)
    action = Column(String)
    lot_size = Column(Float)
    price = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class WebhookLog(Base):
    __tablename__ = "webhook_logs"

    id = Column(Integer, primary_key=True, index=True)
    payload = Column(JSON)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
