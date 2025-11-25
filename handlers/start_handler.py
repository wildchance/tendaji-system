from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Wildchance Trading Bot!\n"
        "📊 Use /history to view signals & trades.\n"
        "💵 Signals coming soon!"
    )
