from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import TradeRequest
from .database import SessionLocal
from .models import TradeLog

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/trade")
def save_trade(request: TradeRequest, db: Session = Depends(get_db)):
    trade = TradeLog(
        symbol=request.symbol,
        action=request.action,
        price=request.price,
        volume=request.volume,
        comment=request.comment
    )
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return {"status": "success", "trade_id": trade.id}
