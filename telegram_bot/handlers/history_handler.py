import os
import requests
from telegram import Update
from telegram.ext import ContextTypes

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/trades")
        data = response.json()

        if not data:
            await update.message.reply_text("📭 No trade history found.")
            return

        message = "📜 Trade History:\n\n"
        for trade in data[-10:]:
            message += f"{trade['pair']} | {trade['action']} | {trade['price']}\n"

        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(f"⚠ Error fetching history: {e}")

