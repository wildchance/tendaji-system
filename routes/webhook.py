from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/")
async def webhook_receiver(request: Request):
    data = await request.json()
    return {"received": data}
