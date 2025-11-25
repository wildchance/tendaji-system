import requests
from telegram import Update
from telegram.ext import ContextTypes

API_URL = "http://127.0.0.1:8000/stats/profit"

async def handle_profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        profit = data.get('profit', 0)
        emoji = "💰" if profit >= 0 else "📉"
        
        await update.message.reply_text(f"{emoji} **Total Profit:** ${profit:.2f} USD")
        
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")
