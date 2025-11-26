import requests
import os
from telegram import Update
from telegram.ext import ContextTypes

API_BASE_URL = os.getenv("API_BASE_URL", "https://wildchance-system-production.up.railway.app")

async def handle_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{API_BASE_URL}/history/trades", timeout=5)

        if response.status_code == 200:
            trades = response.json()

            if not trades:
                await update.message.reply_text("📭 No history found.")
            else:
                msg = "📊 *Recent Trades:*\n\n"
                for trade in trades[:5]:
                    msg += f"🔹 {trade['pair']} | {trade['action']} | Lot {trade['lot_size']} | @ {trade['price']}\n"
                await update.message.reply_text(msg)
        else:
            await update.message.reply_text("⚠ API Error getting trade history.")

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")
