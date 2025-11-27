import os
import asyncio
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)
from handlers.start_handler import start
from handlers.history_handler import handle_history
from handlers.last5_handler import handle_last5
from handlers.profit_handler import handle_profit
from handlers.wins_handler import handle_wins
from handlers.summary_handler import handle_summary
from handlers.admin_handler import handle_admin

API_BASE_URL = "https://wildchance-system-production.up.railway.app"
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register Commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("history", handle_history))
    application.add_handler(CommandHandler("last5", handle_last5))
    application.add_handler(CommandHandler("profit", handle_profit))
    application.add_handler(CommandHandler("wins", handle_wins))
    application.add_handler(CommandHandler("summary", handle_summary))
    application.add_handler(CommandHandler("admin", handle_admin))

    async def echo(update, context):
        if update.message:
            await update.message.reply_text(f"You said: {update.message.text}")

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Telegram Bot is now running 24/7 on PythonAnywhere!")
    await application.initialize()
    await application.start()
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
