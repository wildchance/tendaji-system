from fastapi import FastAPI
from core.signals import router as signals_router
from core.trade import router as trade_router
from core.webhook import router as webhook_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Tendaji Trading Engine is running 🚀"}

app.include_router(signals_router)
app.include_router(trade_router)
app.include_router(webhook_router)
