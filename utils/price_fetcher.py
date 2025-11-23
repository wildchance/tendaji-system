import httpx
import re
from typing import Optional
from decouple import config

API_KEY = config("TWELVEDATA_API_KEY", default=None)
BASE_URL_TWELVE = "https://api.twelvedata.com/price"

BASE_URL_FRANKFURTER = "https://api.frankfurter.app/latest"

async def _frankfurter_price(base: str, quote: str) -> Optional[float]:
    url = f"{BASE_URL_FRANKFURTER}?from={base}&to={quote}"
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            resp = await client.get(url)
            if resp.status_code != 200:
                return None
            data = resp.json()
            return float(data["rates"].get(quote))
    except Exception:
        return None


async def _twelvedata_price(symbol: str) -> Optional[float]:
    if not API_KEY:
        return None
    params = {"symbol": symbol, "apikey": API_KEY}
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(BASE_URL_TWELVE, params=params)
            data = r.json()
            if "price" in data:
                return float(data["price"])
    except Exception:
        return None
    return None

