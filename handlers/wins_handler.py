import requests
from telegram import Update
from telegram.ext import ContextTypes

API_URL = "http://127.0.0.1:8000/stats/wins"

async def handle_wins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(API_URL)
        data = response.json()
        await update.message.reply_text(
            f"📈 Win rate: {data['win_rate']}%\n"
            f"Wins: {data['wins']} | Losses: {data['losses']}"
        )
    except Exception as e:
        await update.message.reply_text(f"⚠ Error: {str(e)}")
