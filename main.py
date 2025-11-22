from fastapi import FastAPI
from core.signals import router as signals_router
from core.trade import router as trade_router
from core.webhook import router as webhook_router
from database.db import init_db
from routes.telegram_routes import router as telegram_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
def home():
    return {"message": "Tendaji Trading Engine Running"}

@app.post("/webhook/signal")
def trading_signal(payload: dict):
    return {"received": payload, "status": "success"}

@app.get("/telegram/send-alert")
def send_alert():
    return {"status": "alert sent"}
    
app.include_router(signals_router)
app.include_router(trade_router)
app.include_router(webhook_router)
app.include_router(telegram_router)
app.include_router(admin_router)
