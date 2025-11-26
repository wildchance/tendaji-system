from telegram import Update
from telegram.ext import ContextTypes
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/summary")
        data = response.json()
        
        msg = (
            "📊 Trade Summary:\n"
            f"Total Trades: {data.get('total_trades', 'N/A')}\n"
            f"Wins: {data.get('wins', 'N/A')}\n"
            f"Losses: {data.get('losses', 'N/A')}\n"
            f"Profit: {data.get('profit', 'N/A')}\n"
        )
    except Exception as e:
        msg = f"❌ Error fetching summary: {e}"

    await update.message.reply_text(msg)
