from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SignalResponse(BaseModel):
    symbol: str
    action: str
    entry_price: float
    stop_loss: float
    take_profit: float
    timestamp: datetime

class TradeRequest(BaseModel):
    signal_id: int
    symbol: str
    action: str
    price: float
    volume: float
    comment: Optional[str] = None

class WebhookRequest(BaseModel):
    chat_id: str
    message: str
