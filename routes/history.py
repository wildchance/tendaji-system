from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.db import get_db
from models.trade_model import TradeLog
from models.signal_model import SignalLog

router = APIRouter()

@router.get("/history/trades")
async def get_trade_history(db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(TradeLog).order_by(TradeLog.id.desc()))
    rows = q.scalars().all()
    return rows

@router.get("/history/signals")
async def get_signal_history(db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(SignalLog).order_by(SignalLog.id.desc()))
    rows = q.scalars().all()
    return rows
