from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class TradeLog(Base):
    __tablename__ = "trade_logs"

    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String, nullable=False)
    action = Column(String, nullable=False)
    lot_size = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
