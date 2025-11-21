from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def webhook_receiver(request: Request):
    payload = await request.json()
    return {"status": "received", "data": payload}
