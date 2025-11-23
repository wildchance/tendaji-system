from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.signal_model import SignalLog
from services.telegram_service import send_telegram_message
from services.whatsapp_service import send_whatsapp_message

router = APIRouter()

class SignalIn(BaseModel):
    symbol: str
    action: str
    strength: int

@router.post("/signal")
async def receive_signal(payload: SignalIn, db: AsyncSession = Depends(get_db)):
    new = SignalLog(symbol=payload.symbol, action=payload.action, strength=payload.strength)
    db.add(new)
    await db.commit()
    await db.refresh(new)

message = f"📢 WildChance Signal: {payload.symbol} | {payload.action} | Strength: {payload.strength}"
    await send_telegram_message(message)

    return {"status": "saved", "id": new.id}
