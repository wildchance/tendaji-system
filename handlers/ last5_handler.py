from telegram import Update
from telegram.ext import ContextTypes
import os
import asyncpg

DB_URL = os.getenv("DATABASE_URL")

async def fetch_last5():
    conn = await asyncpg.connect(DB_URL)
    rows = await conn.fetch(
        "SELECT pair, direction, entry_price, result FROM trades ORDER BY timestamp DESC LIMIT 5"
    )
    await conn.close()
    return rows

async def handle_last5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trades = await fetch_last5()
    
    if not trades:
        await update.message.reply_text("No trades found.")
        return
    
    message = "📊 *Last 5 Trades:*\n\n"
    for t in trades:
        message += f"• {t['pair']} | {t['direction']} | Entry: {t['entry_price']} | Result: {t['result']}\n"
    
    await update.message.reply_text(message, parse_mode="Markdown")
