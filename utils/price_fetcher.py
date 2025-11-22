import httpx
from decouple import config

API_KEY = config("TWELVEDATA_API_KEY", default=None)
BASE_URL = "https://api.twelvedata.com/price"


async def get_forex_price(symbol: str):
    symbol = symbol.strip().upper()

    if not API_KEY or API_KEY == "demo":
        url = f"https://api.exchangerate.host/convert?from={symbol[:3]}&to={symbol[3:]}"
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(url)
                data = r.json()
                return float(data.get("result"))
        except:
            return None

    params = {
        "symbol": symbol,
        "apikey": API_KEY
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_URL, params=params)
            data = response.json()
            return float(data.get("price")) if "price" in data else None
    except:
        return None
