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
    
    symbol = payload.get("symbol") or payload.get("pair") or payload.get("ticker")
    action = payload.get("action") or payload.get("side")
    strength = payload.get("strength") or payload.get("confidence", 0)

    new_signal = SignalLog(symbol=symbol, action=action, strength=int(strength))
    db.add(new_signal)
    await db.commit()
    await db.refresh(new_signal)

    message = f"🔔 Webhook Signal: {symbol} | {action} | Strength: {strength}"
    await send_telegram_message(message)

    return {"status": "saved", "id": new_signal.id}
