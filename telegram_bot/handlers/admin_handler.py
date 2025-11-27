import os
from telegram import Update
from telegram.ext import ContextTypes

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def handle_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Usage:\n/admin <password> <message>")
        return

    password = context.args[0]
    message = " ".join(context.args[1:])

    if password != ADMIN_PASSWORD:
        await update.message.reply_text("⛔ Wrong password")
        return

    await context.bot.send_message(chat_id=CHAT_ID, text=f"📢 ADMIN BROADCAST:\n{message}")

