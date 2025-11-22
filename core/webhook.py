from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.db import get_db
from models.signal_model import SignalLog
from services.telegram_service import send_telegram_message

router = APIRouter()

@router.post("/webhook/signal")
async def webhook_signal(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.json()

    symbol = payload.get("symbol", "")
    action = payload.get("action", "")
    strength = int(payload.get("strength", 0))

    new_signal = SignalLog(symbol=symbol, action=action, strength=strength)
    db.add(new_signal)
    await db.commit()
    await db.refresh(new_signal)

    message = f"🔔 Webhook Signal: {symbol} {action} | Strength: {strength}"
    await send_telegram_message(message)

    return {"status": "success", "received": payload}
