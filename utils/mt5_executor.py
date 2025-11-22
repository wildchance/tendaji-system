import MetaTrader5 as mt5

def init_mt5():
    mt5.initialize()
    account = 12345678 
    password = "YourPassword"
    server = "MetaQuotes-Demo"
    login = mt5.login(account, password=password, server=server)
    return login

def place_order(symbol, action, lot=0.1):
    order_type = mt5.ORDER_BUY if action.lower() == "buy" else mt5.ORDER_SELL
    price = mt5.symbol_info_tick(symbol).ask if order_type==mt5.ORDER_BUY else mt5.symbol_info_tick(symbol).bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "deviation": 10,
    }
    return mt5.order_send(request)
