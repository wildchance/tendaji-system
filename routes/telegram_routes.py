from fastapi import APIRouter, FastAPI
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from handlers.start_handler import start
from handlers.history_handler import handle_history
import asyncio
import os

router = APIRouter()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("history", handle_history))

async def echo(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


async def start_telegram_bot():
    print("🚀 Telegram bot is starting...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    print("🤖 Telegram bot is now running!")


def register_bot(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        asyncio.create_task(start_telegram_bot())
