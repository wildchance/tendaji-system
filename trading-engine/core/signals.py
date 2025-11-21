from fastapi import APIRouter

router = APIRouter()

fake_signals = [
    {"pair": "EURUSD", "signal": "BUY", "strength": 80},
    {"pair": "GBPUSD", "signal": "SELL", "strength": 65}
]

@router.get("/signals")
def get_signals():
    return {"status": "success", "data": fake_signals}
