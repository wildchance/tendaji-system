from telegram import Update
from telegram.ext import ContextTypes

ADMIN_PASSWORD = "12345"  # change later

async def handle_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Usage: /admin <password>")
        return

    if context.args[0] == ADMIN_PASSWORD:
        await update.message.reply_text("🔓 Admin access granted.")
    else:
        await update.message.reply_text("❌ Wrong password.")
