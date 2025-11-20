from pydantic import BaseModel

class Signal(BaseModel):
    symbol: str
    action: str  # buy or sell
    entry: float
    tp: float
    sl: float
