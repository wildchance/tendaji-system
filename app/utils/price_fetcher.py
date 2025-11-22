import requests
import os

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_forex_price(symbol="EURUSD"):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": symbol[:3],
        "to_currency": symbol[3:],
        "apikey": API_KEY
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        price = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        return float(price)
    except:
        return None
