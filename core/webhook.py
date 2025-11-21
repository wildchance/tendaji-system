from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from database.models import WebhookLog

router = APIRouter()

@router.post("/webhook")
async def webhook_receiver(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.json()
    log = WebhookLog(payload=payload)
    db.add(log)
    await db.commit()
    return {"status": "received", "data": payload}
