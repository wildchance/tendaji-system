from fastapi import APIRouter
from pydantic import BaseModel
from services.telegram_service import send_telegram_message

router = APIRouter()

class Alert(BaseModel):
    chat_id: str
    message: str

@router.post("/telegram/send-alert")
def send_alert(alert: Alert):
    response = send_telegram_message(alert.chat_id, alert.message)
    return {"status": "sent", "response": response}
