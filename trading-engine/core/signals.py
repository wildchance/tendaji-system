from fastapi import APIRouter
from .schemas import SignalResponse
from datetime import datetime

router = APIRouter()

@router.get("/signals", response_model=list[SignalResponse])
def get_signals():
    return [
        {
            "symbol": "EURUSD",
            "action": "BUY",
            "entry_price": 1.0723,
            "stop_loss": 1.0680,
            "take_profit": 1.0780,
            "timestamp": datetime.utcnow()
        }
    ]
