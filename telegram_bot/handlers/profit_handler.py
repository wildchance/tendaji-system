import os
import requests
from telegram import Update
from telegram.ext import ContextTypes

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/profit")
        data = response.json()

        await update.message.reply_text(f"💰 Total Profit: {data['profit']} USD")
    except Exception:
        await update.message.reply_text("⚠ Error fetching profit data.")

