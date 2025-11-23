from fastapi import APIRouter, Response
import csv
from io import StringIO
from database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.signal_model import SignalLog

router = APIRouter()

@router.get("/export/signals.csv")
async def export_signals(db: AsyncSession = Depends(get_db)):
    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["ID", "Symbol", "Action", "Strength", "Time"])

    q = await db.execute(select(SignalLog))
    rows = q.scalars().all()
    for r in rows:
        writer.writerow([r.id, r.symbol, r.action, r.strength, r.created_at])
    
    response = Response(content=buffer.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=signals.csv"
    return response
