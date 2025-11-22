from fastapi import APIRouter
from utils.price_fetcher import get_forex_price

router = APIRouter()

@router.get("/price/{symbol}")
async def get_price(symbol: str):
    price = get_forex_price(symbol)
    if price:
        return {"symbol": symbol, "price": price}
    return {"error": "Price not available"}
