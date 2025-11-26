from telegram import Update
from telegram.ext import ContextTypes
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_wins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/wins")
        data = response.json()

        await update.message.reply_text(
            f"🏆 Wins: {data.get('wins', 0)}\n❌ Losses: {data.get('losses', 0)}"
        )
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
