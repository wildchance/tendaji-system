from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    return {
        "status": "Webhook received",
        "data": data
    }
