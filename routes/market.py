from fastapi import APIRouter
from utils.price_fetcher import get_forex_price  # now valid

router = APIRouter()

@router.get("/price/{symbol}")
def get_price(symbol: str):
    result = get_forex_price(symbol.upper())
    if result:
        return result
    return {"error": "Symbol not found or API failed"}
