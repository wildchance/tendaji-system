async def place_order(pair: str, action: str, lot_size: float, price: float):
    print(f"MOCK TRADE => {pair} | {action} | Lot: {lot_size} | Price: {price}")
    return {"status": "success", "pair": pair, "action": action}
