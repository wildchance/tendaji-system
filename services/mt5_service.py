import MetaTrader5 as mt5

async def execute_mt5_trade(symbol, action, lot):
    if not mt5.initialize():
        return {"error": "MT5 failed to initialize"}

    order_type = mt5.ORDER_BUY if action == "BUY" else mt5.ORDER_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "magic": 123456,
        "comment": "Tendaji Auto Trade",
    }

    result = mt5.order_send(request)
    return {"mt5_result": str(result)}
