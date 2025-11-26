from telegram import Update
from telegram.ext import ContextTypes
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/profit")
        msg = f"💰 Total Profit: {response.json().get('profit', 'N/A')}"
    except Exception as e:
        msg = f"❌ Error fetching profit: {e}"

    await update.message.reply_text(msg)
