from fastapi import FastAPI
from routes.signals import router as signals_router
from routes.trade import router as trade_router
from routes.webhook import router as webhook_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 FastAPI Trading Engine Running on Railway!"}

# Include Routes
app.include_router(signals_router)
app.include_router(trade_router)
app.include_router(webhook_router)
