from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def webhook_listener(request: Request):
    data = await request.json()
    return {"received": data}
