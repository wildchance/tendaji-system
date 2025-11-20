from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class Trade(BaseModel):
    symbol: str
    action: str  # BUY or SELL
    price: float
    quantity: float

@router.post("/trade")
def log_trade(trade: Trade):
    return {
        "status": "Trade recorded",
        "trade": trade,
        "recorded_at": datetime.utcnow()
    }
