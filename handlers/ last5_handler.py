from telegram import Update
from telegram.ext import ContextTypes
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "https://wildchance-system-production.up.railway.app")

async def handle_last5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/trades?limit=5")
        trades = response.json()

        if not trades:
            await update.message.reply_text("No recent trades found.")
            return

        message = "📊 *Last 5 Trades:*\n"
        for t in trades:
            message += f"• {t['pair']} {t['action']} at {t['price']} ({t['created_at']})\n"

        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(f"Error fetching data: {e}")
