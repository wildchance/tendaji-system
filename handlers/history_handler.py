from telegram import Update
from telegram.ext import ContextTypes
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send last 10 trades to user"""
    try:
        response = requests.get(f"{API_BASE_URL}/history/trades")
        trades = response.json()

        if not trades:
            await update.message.reply_text("No trade history available.")
            return

        msg = "\n".join([f"{t['pair']} | {t['action']} | {t['price']}" for t in trades[:10]])
        await update.message.reply_text(f"📈 Trade History:\n{msg}")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error fetching history: {e}")
