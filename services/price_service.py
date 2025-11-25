import httpx
from decouple import config

API_KEY = config("TWELVEDATA_API_KEY")

async def get_price(symbol: str):
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        data = r.json()
        return data.get("price")
