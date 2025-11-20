from fastapi import APIRouter
from models.signal import Signal

router = APIRouter()

@router.post("/")
def receive_signal(signal: Signal):
    return {"status": "Signal received", "data": signal}
