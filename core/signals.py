from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ---- Database Setup ----
DATABASE_URL = "postgresql://user:password@db:5432/trading"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# ---- FastAPI Router ----
router = APIRouter()

# ---- Request Model ----
class TradeSignal(BaseModel):
    symbol: str
    action: str  # BUY or SELL
    strength: int

# ---- API Endpoint ----
@router.post("/signal")
async def receive_signal(signal: TradeSignal):
    return {
        "status": "received",
        "symbol": signal.symbol,
        "action": signal.action,
        "strength": signal.strength
    }
