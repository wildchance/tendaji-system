from fastapi import APIRouter, FastAPI
from telegram import Update
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
import threading

router = APIRouter()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Telegram Handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("history", handle_history))

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Background bot runner
def start_telegram_bot():
    print("🚀 Telegram bot is running...")
    thread = threading.Thread(target=application.run_polling, daemon=True)
    thread.start()

# Register with FastAPI
def register_bot(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        start_telegram_bot()
