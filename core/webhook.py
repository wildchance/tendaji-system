from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.signal_model import SignalLog
from services.telegram_service import send_telegram_message

router = APIRouter()

@router.post("/webhook/signal")
async def webhook_signal(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.json()

 symbol = payload.get("symbol") or payload.get("pair") or payload.get("ticker")
    action = payload.get("action")
    strength = payload.get("strength", 0)

    new = SignalLog(symbol=symbol, action=action, strength=int(strength or 0))
    db.add(new)
    await db.commit()
    await db.refresh(new)

    msg = f"🔔 Webhook signal: {symbol} {action} (strength {strength})"
    await send_telegram_message(msg)
    return {"status": "ok", "id": new.id}
