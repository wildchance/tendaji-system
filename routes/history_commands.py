from fastapi import APIRouter
from services.telegram_service import send_telegram_message
from database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.trade_model import TradeLog

router = APIRouter()

@router.get("/history/latest")
async def get_latest_trade(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TradeLog).order_by(TradeLog.id.desc()).limit(1))
    trade = result.scalar_one_or_none()

    if trade:
        message = (
            f"📊 Latest Trade\n"
            f"Pair: {trade.pair}\nAction: {trade.action}\n"
            f"Lot: {trade.lot_size}  Price: {trade.price}\n"
            f"Time: {trade.created_at}\n"
            f"🚀 Wildchance Signals"
        )
        await send_telegram_message(message)
        return {"status": "sent"}
    return {"error": "No trades found"}
