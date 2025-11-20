from pydantic import BaseModel

class Trade(BaseModel):
    symbol: str
    volume: float
    trade_type: str
    price: float | None
