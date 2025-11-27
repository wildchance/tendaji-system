import os
import requests
from telegram import Update
from telegram.ext import ContextTypes

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_last5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/last5")
        data = response.json()

        if not data:
            await update.message.reply_text("📭 No recent trades found.")
            return

        msg = "📊 Last 5 Trades:\n\n"
        for trade in data:
            msg += f"{trade['pair']} — {trade['action']} — {trade['price']}\n"

        await update.message.reply_text(msg)
    except Exception:
        await update.message.reply_text("⚠ Error fetching last5 trades.")

