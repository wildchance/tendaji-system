from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Tendaji Trading Engine Running"}

@app.post("/webhook/signal")
def trading_signal(payload: dict):
    return {"received": payload, "status": "success"}

@app.get("/telegram/send-alert")
def send_alert():
    return {"status": "alert sent"}
