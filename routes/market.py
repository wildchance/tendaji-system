from fastapi import APIRouter, HTTPException
from typing import Dict
from utils.price_fetcher import get_forex_price
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database.db import get_db
from sqlalchemy import select
from models.signal_model import SignalLog
from models.trade_model import TradeLog

router = APIRouter(prefix="")

@router.get("/price/{pair}")
async def price(pair: str):
    p = pair.strip().upper()
    price = await get_forex_price(p)
    if price is None:
        raise HTTPException(status_code=404, detail="symbol not found")
    return {"pair": p, "price": price}

@router.get("/dashboard")
async def dashboard_html():
    return {"info": "open /static/dashboard/index.html in your browser"}

@router.get("/api/signals")
async def api_signals(limit: int = 50, db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(SignalLog).order_by(SignalLog.id.desc()).limit(limit))
    rows = q.scalars().all()
    return [{"id": r.id, "symbol": r.symbol, "action": r.action, "strength": r.strength, "created_at": str(r.created_at)} for r in rows]

@router.get("/api/trades")
async def api_trades(limit: int = 50, db: AsyncSession = Depends(get_db)):
    q = await db.execute(select(TradeLog).order_by(TradeLog.id.desc()).limit(limit))
    rows = q.scalars().all()
    return [{"id": r.id, "pair": r.pair, "action": r.action, "lot_size": r.lot_size, "price": r.price, "created_at": str(r.created_at)} for r in rows]
