import httpx
import re
from typing import Optional

async def get_forex_price(pair: str) -> Optional[float]:
    """
    Return latest price for a pair like 'EURUSD', 'GBPUSD', or 'XAUUSD'.
    Strategy:
      - If pair is 6 chars (e.g. EURUSD), call exchangerate.host convert endpoint.
      - If pair starts with XAU or XAG, try metals.live API as a free fallback.
      - Return None if not available.
    """
    pair = pair.strip().upper()
   
    pair_clean = pair.replace("/", "")
  
    if re.fullmatch(r"[A-Z]{6}", pair_clean):
        base = pair_clean[:3]
        quote = pair_clean[3:]
        url = f"https://api.exchangerate.host/convert?from={base}&to={quote}"
        try:
            async with httpx.AsyncClient(timeout=8) as client:
                r = await client.get(url)
                data = r.json()
                if data.get("success") is True:
                    return float(data["result"])
             
                if "result" in data:
                    return float(data["result"])
        except Exception:
            return None

  
    if pair_clean.startswith("XAU") or pair_clean.startswith("XAG"):
      
        try:
            async with httpx.AsyncClient(timeout=8) as client:
                r = await client.get("https://api.metals.live/v1/spot")
                arr = r.json()
              
                for item in arr:
                    if isinstance(item, dict):
                       
                        sym = item.get("symbol") or item.get("metal") or item.get("pair")
                        price = item.get("price") or item.get("last") or item.get("value")
                        if not sym:
                           
                            for k, v in item.items():
                                if isinstance(v, (int, float)) and (k.upper().startswith("XAU") or k.upper().startswith("XAG")):
                                    return float(v)
                        if sym and sym.upper() == pair_clean:
                            return float(price)
              
        except Exception:
            return None

    m = re.match(r"([A-Z]{3})[^A-Z0-9]*([A-Z]{3})", pair.upper())
    if m:
        base, quote = m.group(1), m.group(2)
        url = f"https://api.exchangerate.host/convert?from={base}&to={quote}"
        try:
            async with httpx.AsyncClient(timeout=8) as client:
                r = await client.get(url)
                data = r.json()
                return float(data.get("result"))
        except Exception:
            return None

    return None
