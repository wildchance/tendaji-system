from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.trade import TradeLog

router = APIRouter()

class Trade(BaseModel):
    pair: str
    action: str
    lot_size: float
    price: float

@router.post("/trade")
async def create_trade(trade: Trade, db: AsyncSession = Depends(get_db)):
    trade_data = TradeLog(**trade.dict())
    db.add(trade_data)
    await db.commit()
    await db.refresh(trade_data)
    return {"status": "success", "data": trade_data}
