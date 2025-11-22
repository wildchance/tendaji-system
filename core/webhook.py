from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.signal_model import SignalLog
from services.telegram_service import send_telegram_message

router = APIRouter(prefix="/webhook")

@router.post("/signal")
async def webhook_signal(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.json()
   
    symbol = payload.get("symbol") or payload.get("ticker") or payload.get("pair") or payload.get("instrument")
    action = payload.get("action") or payload.get("order") or payload.get("side")
   
    strength = payload.get("strength") or payload.get("contracts") or payload.get("qty") or payload.get("size") or 0

    if not symbol or not action:
        # return the raw payload for debugging if missing fields
        return {"received": payload, "status": "missing_fields"}

    new = SignalLog(symbol=symbol, action=action, strength=int(strength or 0))
    db.add(new)
    await db.commit()
    await db.refresh(new)

    
    message = f"🔔 Webhook: {symbol} {action} (strength {strength})"
    await send_telegram_message(message)

    return {"received": {"symbol": symbol, "action": action, "strength": strength}, "status": "success"}
