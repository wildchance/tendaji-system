from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.signal import SignalLog
from services.telegram_service import send_telegram_message

router = APIRouter()

@router.post("/signal")
async def receive_signal(symbol: str, action: str, strength: int, db: AsyncSession = Depends(get_db)):
    new_signal = SignalLog(symbol=symbol, action=action, strength=strength)
    db.add(new_signal)
    await db.commit()
    await db.refresh(new_signal)

    message = f"📢 Signal: {symbol} | {action} | Strength: {strength}"
    await send_telegram_message(message)
