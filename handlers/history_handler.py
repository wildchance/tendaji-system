from telegram import Update
from telegram.ext import ContextTypes
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "https://wildchance-system-production.up.railway.app")

async def handle_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"{API_BASE_URL}/history/trades")
    data = response.json()

    if not data:
        await update.message.reply_text("📭 No trade history found yet.")
        return

    message = "📜 *Recent Trades:*\n\n"
    for trade in data[-5:]:
        message += f"• {trade['pair']} | {trade['action']} | Lot {trade['lot_size']}\n"
    
    await update.message.reply_text(message)
