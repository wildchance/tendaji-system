from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from sqlalchemy import select
from models.signal_model import SignalLog
from models.trade_model import TradeLog

router = APIRouter(prefix="/export")

@router.get("/signals")
async def export_signals(db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(SignalLog))
    rows = q.scalars().all()
    return [
        {"id": r.id, "symbol": r.symbol, "action": r.action, "strength": r.strength, "created_at": str(r.created_at)}
        for r in rows
    ]

@router.get("/trades")
async def export_trades(db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(TradeLog))
    rows = q.scalars().all()
    return [
        {"id": r.id, "pair": r.pair, "action": r.action, "lot_size": r.lot_size, "price": r.price, "created_at": str(r.created_at)}
        for r in rows
    ]
