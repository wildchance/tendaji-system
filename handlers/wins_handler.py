from telegram import Update
from telegram.ext import ContextTypes
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_wins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/wins")
        msg = f"🏆 Total Wins: {response.json().get('wins', 'N/A')}"
    except Exception as e:
        msg = f"❌ Error fetching wins: {e}"

    await update.message.reply_text(msg)
