from fastapi import APIRouter, FastAPI
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from handlers.start_handler import start
from handlers.history_handler import handle_history
from handlers.last5_handler import handle_last5
from handlers.profit_handler import handle_profit
from handlers.wins_handler import handle_wins
from handlers.summary_handler import handle_summary
from handlers.admin_handler import handle_admin
import asyncio
import os

router = APIRouter()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Register all command handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("history", handle_history))
application.add_handler(CommandHandler("last5", handle_last5))
application.add_handler(CommandHandler("profit", handle_profit))
application.add_handler(CommandHandler("wins", handle_wins))
application.add_handler(CommandHandler("summary", handle_summary))
application.add_handler(CommandHandler("admin", handle_admin))

# Safe echo handler — prevents crash from NoneType
async def echo(update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(f"You said: {update.message.text}")

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


# Correct async Telegram bot startup
async def start_telegram_bot():
    print("🚀 Telegram bot is starting...")
    try:
        await application.initialize()
        await application.start()
        await application.run_polling()  # <-- Correct for v20+
        print("🤖 Telegram bot is now running and receiving messages...")
    except Exception as e:
        print(f"❌ Telegram bot failed to start: {e}")


# Register bot with FastAPI (startup & shutdown)
def register_bot(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        asyncio.create_task(start_telegram_bot())

    @app.on_event("shutdown")
    async def shutdown_event():
        print("🛑 Shutting down Telegram bot...")
        try:
            await application.stop()
            await application.shutdown()
            print("✅ Telegram bot stopped successfully")
        except Exception as e:
            print(f"❌ Error stopping bot: {e}")


# API endpoint to send alerts from backend to Telegram
@router.post("/send_alert")
async def send_alert(message: dict):
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if chat_id:
        try:
            await application.bot.send_message(chat_id=chat_id, text=message["message"])
            return {"status": "Alert sent"}
        except Exception as e:
            return {"status": "Failed", "error": str(e)}
    return {"status": "No chat_id configured"}
