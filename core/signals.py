from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.db import get_db
from models.signal import SignalLog

router = APIRouter()

class TradeSignal(BaseModel):
    symbol: str
    action: str
    strength: int

@router.post("/signal")
async def receive_signal(signal: TradeSignal, db: Session = Depends(get_db)):
    new_signal = SignalLog(
        symbol=signal.symbol,
        action=signal.action,
        strength=signal.strength
    )
    db.add(new_signal)
    db.commit()
    db.refresh(new_signal)

    return {
        "status": "saved",
        "data": {
            "id": new_signal.id,
            "symbol": new_signal.symbol,
            "action": new_signal.action,
            "strength": new_signal.strength
        }
    }
