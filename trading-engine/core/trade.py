from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Trade(BaseModel):
    pair: str
    action: str
    lot_size: float
    price: float

@router.post("/trade")
def create_trade(trade: Trade):
    return {
        "status": "success",
        "message": "Trade logged",
        "data": trade
    }
