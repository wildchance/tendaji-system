from database.db import SessionLocal
from models.trade_logs import TradeLog
from models.signal_logs import SignalLog

async def handle_summary(update, context):
    db = SessionLocal()
    
    total_trades = db.query(TradeLog).count()
    wins = db.query(TradeLog).filter(TradeLog.action=="WIN").count()
    losses = db.query(TradeLog).filter(TradeLog.action=="LOSS").count()
    
    win_rate = round((wins/total_trades)*100, 2) if total_trades else 0
    
    msg = f"""
📊 *WILDCHANCE SYSTEM SUMMARY*
Total Trades: {total_trades}
Wins: {wins}
Losses: {losses}
Win Rate: {win_rate}%
🔥 Performance Strong!
"""
    await update.message.reply_text(msg, parse_mode="Markdown")
    db.close()
