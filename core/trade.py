from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.trade_model import TradeLog
from services.telegram_service import send_telegram_message

router = APIRouter()

class TradeIn(BaseModel):
    pair: str
    action: str
    lot_size: float
    price: float

@router.post("/trade")
async def receive_trade(payload: TradeIn, db: AsyncSession = Depends(get_db)):
    new_trade = TradeLog(
        pair=payload.pair,
        action=payload.action,
        lot_size=payload.lot_size,
        price=payload.price
    )

    db.add(new_trade)
    await db.commit()
    await db.refresh(new_trade)

    message = (
        f"💹 wildchance Trade Executed:\n"
        f"Pair: {payload.pair}\n"
        f"Action: {payload.action}\n"
        f"Lot Size: {payload.lot_size}\n"
        f"Price: {payload.price}"
    )

    await send_telegram_message(message)

    return {"status": "saved", "id": new_trade.id}
