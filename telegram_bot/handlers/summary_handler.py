import os
import requests
from telegram import Update
from telegram.ext import ContextTypes

API_BASE_URL = os.getenv("API_BASE_URL")

async def handle_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/summary")
        data = response.json()

        msg = f"""
📈 Trade Summary:
-----------------
Total Trades: {data['total_trades']}
Wins: {data['wins']}
Losses: {data['losses']}
Profit: ${data['profit']}
"""
        await update.message.reply_text(msg)
    except:
        await update.message.reply_text("⚠ Error fetching summary.")

