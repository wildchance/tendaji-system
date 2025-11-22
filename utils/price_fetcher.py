import requests

API_URL = "https://api.exchangerate.host/latest"

def get_forex_price(symbol: str):
    """
    Fetch live forex price using exchangerate.host free API.
    Format: symbol must be like 'EURUSD', 'GBPJPY', 'XAUUSD'
    """
    base = symbol[:3] 
    quote = symbol[3:] 

    url = f"{API_URL}?base={base}&symbols={quote}"

    response = requests.get(url)
    data = response.json()

    if "rates" not in data or quote not in data["rates"]:
        return None

    return {
        "symbol": symbol,
        "price": data["rates"][quote]
    }
