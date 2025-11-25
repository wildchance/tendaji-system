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
    if update.message:
        await update.message.reply_text(f"You said: {update.message.text}")

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

async def start_telegram_bot():
    """Start Telegram bot without blocking the event loop"""
    print("🚀 Telegram bot is starting...")
    
    try:
        await application.initialize()
        
        await application.start()
        
        await application.updater.start_polling(
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"]
        )
        
        print("✅ Telegram bot is now running!")
        
    except Exception as e:
        print(f"❌ Error starting Telegram bot: {e}")

def register_bot(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        # Create background task for the bot
        asyncio.create_task(start_telegram_bot())
    
    @app.on_event("shutdown")
    async def shutdown_event():
        """Gracefully shutdown the bot"""
        print("🛑 Shutting down Telegram bot...")
        try:
            if application.updater.running:
                await application.updater.stop()
            if application.running:
                await application.stop()
            await application.shutdown()
            print("✅ Telegram bot stopped successfully")
        except Exception as e:
            print(f"❌ Error stopping bot: {e}")
