from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.trade import TradeLog
from services.telegram_service import send_telegram_message

router = APIRouter()

@router.post("/trade")
async def receive_trade(pair: str, action: str, lot_size: float, price: float, db: AsyncSession = Depends(get_db)):
    new_trade = TradeLog(pair=pair, action=action, lot_size=lot_size, price=price)
    db.add(new_trade)
    await db.commit()
    await db.refresh(new_trade)

    # Send Telegram alert
    message = f"💹 Trade Executed: {pair} {action} | Lot: {lot_size} | Price: {price}"
    await send_telegram_message(message)

    return {"status": "saved", "trade_id": new_trade.id}
