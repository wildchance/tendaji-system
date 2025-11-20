from pydantic import BaseModel
from datetime import datetime

class TradeJournalCreate(BaseModel):
    signal: str
    action: str
    price: float

class TradeJournalResponse(BaseModel):
    id: int
    signal: str
    action: str
    price: float
    status: str
    timestamp: datetime

    class Config:
        orm_mode = True
