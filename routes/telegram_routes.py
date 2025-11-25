from fastapi import APIRouter
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from handlers.start_handler import start
from handlers.history_handler import handle_history
import os

router = APIRouter()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Build Telegram Bot Application
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Register Command Handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("history", handle_history))

# Example text echo handler
async def echo(update, context):
    await update.message.reply_text(f"You said: {update.message.text}")

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


@router.on_event("startup")
async def start_telegram_bot():
    print("🚀 Telegram bot is running...")
    application.run_polling()
