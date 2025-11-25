import requests
from fastapi import APIRouter
from telegram import Update
from telegram.ext import CallbackContext

router = APIRouter()

API_BASE_URL = "https://wildchance-system-production.up.railway.app"

def format_history(data):
    if not data:
        return "📭 No history available yet."
    
    history_text = "📊 Wildchance Trade History\n\n"
    for i, item in enumerate(data[:5], start=1):
        if "symbol" in item:
            history_text += f"{i}️⃣ {item['symbol']} | {item['action']} | Strength {item['strength']}\n"
        else:
            history_text += f"{i}️⃣ {item['pair']} | {item['action']} | Lot {item['lot_size']} | Price {item['price']}\n"
    return history_text + "\n🚀 Powered by Wildchance"

def get_latest_history(endpoint):
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}")
        if response.status_code == 200:
            return response.json()
    except Exception:
        return []
    return []

def handle_history(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id

    signals = get_latest_history("/history/signals")
    trades = get_latest_history("/history/trades")

    message = "📜 *History Summary*\n\n"
    message += format_history(signals)
    message += "\n"
    message += format_history(trades)

    context.bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")
