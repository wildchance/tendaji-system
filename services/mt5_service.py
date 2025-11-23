import MetaTrader5 as mt5
import os

MT5_LOGIN = os.getenv("MT5_LOGIN")
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

def connect_mt5():
    if not mt5.initialize(login=int(MT5_LOGIN), password=MT5_PASSWORD, server=MT5_SERVER):
        raise Exception(f"⛔ MT5 Login Failed: {mt5.last_error()}")
    return True

def place_order(symbol, action, lot=0.10):
    connect_mt5()

    trade_type = mt5.ORDER_BUY if action == "BUY" else mt5.ORDER_SELL

    price = mt5.symbol_info_tick(symbol).ask if action == "BUY" else mt5.symbol_info_tick(symbol).bid

    order = mt5.OrderSendRequest(
        action=mt5.TRADE_ACTION_DEAL,
        symbol=symbol,
        volume=lot,
        type=trade_type,
        price=price,
        magic=123456,
        deviation=10,
        comment="Tendaji Auto Trade",
    )
