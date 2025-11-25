from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from routes.history_commands import handle_history

def setup_telegram_bot():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CommandHandler("history", handle_history))

    updater.start_polling()
    return updater
