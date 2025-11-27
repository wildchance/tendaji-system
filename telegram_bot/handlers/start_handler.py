from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Welcome to WildChance Trading Bot! 🎯\n\nUse:\n/history\n/profit\n/wins\n/last5\n/summary")
