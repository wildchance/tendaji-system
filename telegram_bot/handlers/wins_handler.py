import os
import requests
from telegram import Update
from telegram.ext import ContextTypes

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_wins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/wins")
        data = response.json()
        await update.message.reply_text(f"🏆 Winning Trades: {data['wins']}")
    except:
        await update.message.reply_text("⚠ Error fetching wins.")

