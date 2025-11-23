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


async def _metals_price(pair_clean: str) -> Optional[float]:
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get("https://api.metals.live/v1/spot")
            arr = r.json()
            for item in arr:
                if isinstance(item, dict):
                    sym = item.get("symbol") or item.get("metal") or item.get("pair")
                    price = item.get("price") or item.get("last") or item.get("value")
                    if sym and sym.upper() == pair_clean:
                        return float(price)
    except Exception:
        return None
    return None


async def get_forex_price(pair: str) -> Optional[float]:
    pair_clean = pair.strip().upper().replace("/", "")

    price = await _twelvedata_price(pair_clean)
    if price:
        return price

    if re.fullmatch(r"[A-Z]{6}", pair_clean):
        base, quote = pair_clean[:3], pair_clean[3:]
        price = await _frankfurter_price(base, quote)
        if price:
            return price

    if pair_clean.startswith("XAU") or pair_clean.startswith("XAG"):
        return await _metals_price(pair_clean)

    return None
