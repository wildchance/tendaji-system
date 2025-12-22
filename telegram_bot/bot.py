import os
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

from handlers.start_handler import start
from handlers.history_handler import handle_history
from handlers.profit_handler import handle_profit
from handlers.last5_handler import handle_last5
from handlers.wins_handler import handle_wins
from handlers.summary_handler import handle_summary
from handlers.admin_handler import handle_admin


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    print("🚀 Starting Telegram bot...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("history", handle_history))
    app.add_handler(CommandHandler("profit", handle_profit))
    app.add_handler(CommandHandler("last5", handle_last5))
    app.add_handler(CommandHandler("wins", handle_wins))
    app.add_handler(CommandHandler("summary", handle_summary))
    app.add_handler(CommandHandler("admin", handle_admin))

    async def echo(update, context: ContextTypes.DEFAULT_TYPE):
        if update.message:
            await update.message.reply_text(update.message.text)

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Bot running. Press CTRL+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
