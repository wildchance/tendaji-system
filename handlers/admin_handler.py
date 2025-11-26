from telegram import Update
from telegram.ext import ContextTypes

ADMIN_PASSWORD = "12345"   # Change this later!

async def handle_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or args[0] != ADMIN_PASSWORD:
        await update.message.reply_text("🚫 Access Denied. Use /admin <password>")
        return

    await update.message.reply_text("✅ Admin Access Granted! Available commands:\n"
                                    "/broadcast <msg>\n"
                                    "/reset\n"
                                    "/shutdown")
