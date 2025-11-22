from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.signals import router as signals_router
from core.trade import router as trade_router
from core.webhook import router as webhook_router
from database.db import init_db
from routes.telegram_routes import router as telegram_router
from routes.admin import router as admin_router

from routes.market import router as market_router
app.include_router(market_router)

app = FastAPI(title="Tendaji Trading Engine")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
def home():
    return {"message": "Tendaji system API is live"}

@app.post("/webhook/signal")
async def trading_signal(payload: dict):
    return {"received": payload, "status": "success"}

app.include_router(signals_router)
app.include_router(trade_router)
app.include_router(webhook_router)
app.include_router(telegram_router)
app.include_router(admin_router)
app.include_router(market_router)
