from fastapi import APIRouter, Depends, Response
from sqlalchemy import select
from database.db import get_db
from models.trade_model import TradeLog
from io import StringIO
import csv

router = APIRouter(prefix="/export")

@router.get("/trades.csv")
async def export_trades(limit: int = 1000, db = Depends(get_db)):
    q = await db.execute(select(TradeLog).order_by(TradeLog.id.desc()).limit(limit))
    rows = q.scalars().all()
    sio = StringIO()
    writer = csv.writer(sio)
    writer.writerow(["id","pair","action","lot_size","price","created_at"])
    for r in rows:
        writer.writerow([r.id, r.pair, r.action, r.lot_size, r.price, r.created_at])
    return Response(content=sio.getvalue(), media_type="text/csv")
