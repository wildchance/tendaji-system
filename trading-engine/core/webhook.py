from fastapi import APIRouter
from .schemas import WebhookRequest

router = APIRouter()

@router.post("/webhook")
def receive_message(data: WebhookRequest):
    print(f"Received webhook: {data.message}")
    return {"status": "received", "message": data.message}
