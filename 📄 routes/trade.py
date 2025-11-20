from fastapi import APIRouter
from models.trade import Trade
from services.trade_executor import execute_trade

router = APIRouter()

@router.post("/")
def place_trade(trade: Trade):
    result = execute_trade(trade)
    return {"status": "Trade executed", "result": result}
