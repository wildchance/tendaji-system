from fastapi import APIRouter
router = APIRouter()

@router.get("/signals")
def get_signals():
    return {"signals": ["BUY_EURUSD", "SELL_GBPUSD", "BUY_BTCUSD"]}
