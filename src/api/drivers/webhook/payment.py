import asyncio

import httpx
from fastapi import APIRouter, HTTPException, Request

router = APIRouter()


@router.post("/api/v1/payment-status")
async def receive_payment_status(request: Request):
    try:
        data = await request.json()
        result = data["payment_status"]
        print(f"Payment result {result}")
    except Exception:
        raise HTTPException(status_code=500, detail="Server Error")


WEBHOOK_URL = "http://localhost:8001/set-webhook"


async def register_webhook_payment_server():
    params = {
        "user_id": "0",
    }
    body = {
        "webhook_url": "http://localhost:8000/api/v1/payment-status"
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(WEBHOOK_URL, params=params, json=body)
        print(resp)
        if (resp.status_code != 200):
            print(f"Failed to register webhook in the payment mock server: {WEBHOOK_URL}")


asyncio.run(register_webhook_payment_server())
