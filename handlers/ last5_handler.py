import requests
from telegram import Update
from telegram.ext import ContextTypes

API_URL = "http://127.0.0.1:8000/history/trades/last5"

async def handle_last5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(API_URL)
        trades = response.json()
        
        if not trades:
            await update.message.reply_text("📭 No recent trades found.")
            return
        
        message = "📊 **Last 5 Trades:**\n\n"
        for t in trades:
            message += f"🔹 {t['pair']} | {t['action']} | Lot {t['lot_size']} | Price {t['price']} | {t['created_at']}\n"
        
        await update.message.reply_text(message)
        
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")
