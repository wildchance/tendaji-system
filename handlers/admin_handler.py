from telegram import Update
from telegram.ext import ContextTypes

ADMIN_PASSWORD = "1234" # change to .env later

async def handle_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("🔐 Enter password: /admin <password>")
        return
    
    if context.args[0] == ADMIN_PASSWORD:
        await update.message.reply_text("🛡 You are now admin! Access granted.")
    else:
        await update.message.reply_text("❌ Wrong password.")
