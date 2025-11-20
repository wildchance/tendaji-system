from fastapi import APIRouter

router = APIRouter()

@router.get("/signals")
def get_signals():
    return {
        "symbol": "EURUSD",
        "signal": "BUY",
        "entry_price": 1.0840,
        "take_profit": 1.0900,
        "stop_loss": 1.0800,
        "timestamp": "2025-11-21T10:30:00Z"
    }
