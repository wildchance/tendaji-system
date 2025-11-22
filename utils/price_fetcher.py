import httpx
import re
from typing import Optional
from decouple import config

API_KEY = config("TWELVEDATA_API_KEY", default=None)
TD_BASE_URL = "https://api.twelvedata.com/price"


async def get_twelvedata_price(symbol: str) -> Optional[float]:
    """Try fetching price using TwelveData (if API key available)."""
    if not API_KEY:
        return None

    params = {"symbol": symbol, "apikey": API_KEY}

    try:
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(TD_BASE_URL, params=params)
            data = r.json()
            if "price" in data:
                return float(data["price"])
    except Exception:
        return None
    return None


async def get_metals_live_price(symbol: str) -> Optional[float]:
    """Get Gold/Silver spot prices from metals.live free endpoint."""
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get("https://api.metals.live/v1/spot")
            arr = r.json()
            for item in arr:
                if isinstance(item, dict):
                    sym = item.get("symbol") or item.get("metal") or item.get("pair")
                    price = item.get("price") or item.get("last") or item.get("value")
                    if sym and sym.upper() == symbol:
                        return float(price)
                    for k, v in item.items():
                        if isinstance(v, (int, float)) and k.upper() == symbol:
                            return float(v)
    except Exception:
        return None
    return None


async def get_exchangerate_price(pair: str) -> Optional[float]:
    """Free price API via exchangerate.host"""
    base = pair[:3]
    quote = pair[3:]
    url = f"https://api.exchangerate.host/convert?from={base}&to={quote}"
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(url)
            data = r.json()
            if "result" in data:
                return float(data["result"])
    except Exception:
        return None
    return None


async def get_forex_price(pair: str) -> Optional[float]:
    """
    Final smart price fetcher with priority:
    1️⃣ TwelveData API (if key exists)
    2️⃣ Exchangerate.host for forex
    3️⃣ Metals.live for Gold/Silver
    """
    pair = pair.strip().upper()
    pair_clean = pair.replace("/", "")

    if API_KEY:
        td_price = await get_twelvedata_price(pair_clean)
        if td_price:
            return td_price

    if re.fullmatch(r"[A-Z]{6}", pair_clean):
        fx_price = await get_exchangerate_price(pair_clean)
        if fx_price:
            return fx_price

    if pair_clean.startswith("XAU") or pair_clean.startswith("XAG") or "GOLD" in pair_clean:
        metal_price = await get_metals_live_price(pair_clean)
        if metal_price:
            return metal_price

    m = re.match(r"([A-Z]{3})[^A-Z0-9]*([A-Z]{3})", pair_clean)
    if m:
        base, quote = m.group(1), m.group(2)
        return await get_exchangerate_price(base + quote)

    return None
