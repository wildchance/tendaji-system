import requests
from telegram import Update
from telegram.ext import ContextTypes

API_URL = "http://127.0.0.1:8000/stats/summary"

async def handle_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(API_URL)
        data = response.json()
        await update.message.reply_text(
            f"📊 TRADING SUMMARY\n"
            f"💰 Profit: {data['profit']} USD\n"
            f"📈 Win rate: {data['win_rate']}%\n"
            f"📉 Total trades: {data['total_trades']}\n"
            f"🕒 Last trade: {data['last_trade']}"
        )
    except Exception as e:
        await update.message.reply_text(f"⚠ Error: {str(e)}")
