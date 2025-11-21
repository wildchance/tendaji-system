from fastapi import APIRouter
from pydantic import BaseModel
import requests
from decouple import config

router = APIRouter()

BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

class Alert(BaseModel):
    chat_id: str
    message: str

@router.post("/telegram/send-message")
def send_message(alert: Alert):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": alert.chat_id,
        "text": alert.message
    }
    response = requests.post(url, json=payload)
    return response.json()
