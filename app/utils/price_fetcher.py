import httpx
from decouple import config

API_KEY = config("TWELVEDATA_API_KEY", default=None)

async def get_forex_price(symbol: str):
    symbol = symbol.upper()

    if API_KEY:
        url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                r = await client.get(url)
                data = r.json()
                if "price" in data:
                    return float(data["price"])
        except:
            pass

    url = f"https://api.frankfurter.app/latest?from={symbol[:3]}&to={symbol[3:]}"
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(url)
            data = r.json()
            return float(data["rates"][symbol[3:]])
    except:
        return None
