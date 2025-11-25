import httpx
from decouple import config

BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
CHAT_ID = config("TELEGRAM_CHAT_ID")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

async def send_telegram_message(payload: dict):
    message = (
        "📢 *Wildchance Signal Alert*\n\n"
        f"🔹 *Pair:* {payload.get('pair') or payload.get('symbol')}\n"
        f"🔹 *Action:* {payload.get('action')}\n"
        f"🔹 *Lot Size:* {payload.get('lot_size', 'N/A')}\n"
        f"🔹 *Price:* {payload.get('price', 'N/A')}\n\n"
        "🚀 *Stay Profitable with Wildchance Alerts*"
    )

    async with httpx.AsyncClient() as client:
        await client.post(
            TELEGRAM_API,
            json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        )
