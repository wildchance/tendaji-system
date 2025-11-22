import os
import httpx
from decouple import config

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or config("TELEGRAM_BOT_TOKEN", default=None)
DEFAULT_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") or config("TELEGRAM_CHAT_ID", default=None)

async def send_telegram_message(message: str, chat_id: str | None = None):
    if chat_id is None:
        chat_id = DEFAULT_CHAT_ID
    if not TELEGRAM_BOT_TOKEN or not chat_id:
        # no token/chat configured — just log and skip
        print("Telegram not configured (missing token/chat_id). message:", message)
        return {"ok": False, "error": "missing_telegram_config"}

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": str(chat_id), "text": message}

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(url, json=payload)
        try:
            return resp.json()
        except Exception:
            return {"ok": False, "status_code": resp.status_code, "text": resp.text}
