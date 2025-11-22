from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from models.trade_model import TradeLog
from models.signal_model import SignalLog
from sqlalchemy import select

router = APIRouter(prefix="/admin")

@router.get("/signals")
async def list_signals(limit: int = 50, db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(SignalLog).order_by(SignalLog.id.desc()).limit(limit))
    rows = q.scalars().all()
    return {"count": len(rows), "data": [dict(id=r.id, symbol=r.symbol, action=r.action, strength=r.strength, created_at=str(r.created_at)) for r in rows]}

@router.get("/trades")
async def list_trades(limit: int = 50, db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(TradeLog).order_by(TradeLog.id.desc()).limit(limit))
    rows = q.scalars().all()
    return {"count": len(rows), "data": [dict(id=r.id, pair=r.pair, action=r.action, lot_size=r.lot_size, price=r.price, created_at=str(r.created_at)) for r in rows]}
