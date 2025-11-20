from fastapi import FastAPI
from .routes import signals, trade, webhook
from .db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(signals.router)
app.include_router(trade.router)
app.include_router(webhook.router)

@app.get("/")
def home():
    return {"message": "Trading Engine Live!"}
