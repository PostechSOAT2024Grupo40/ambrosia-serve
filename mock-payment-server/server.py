from typing import Annotated, Literal

import httpx
import uvicorn
from fastapi import Body, FastAPI
from pydantic import BaseModel

fake_db = {}


async def set_webhook_url_for_user_payment(user_id: int, webhook_url: str):
    fake_db[user_id] = webhook_url


async def get_webhook_urls():
    return list(fake_db.values())


class Payment(BaseModel):
    user_id: str
    user_amount: float
    total_sale_amount: float


class WebHookResponse(BaseModel):
    status: Literal["ok", "error"]


app = FastAPI()


@app.webhooks.post("payment-status-webhook")
async def payment_webhook(paymeny_data: Payment):
    """_summary_
    When a payment is requested we'll send a POST request with this
    data to the URL that was registerd for the event "payment-status-webhook" via "set-webhook"
    endpoint.

    Args:
        paymeny_data (Payment): _description_
    """

    pass


@app.post("/set-webhook")
async def set_webhook(
    user_id: int,
    webhook_url: Annotated[
        str,
        Body(
            description="See info about webhook at 'Webhooks\\payment-status-webhook' section",
            embed=True,
        )
    ],
):
    await set_webhook_url_for_user_payment(user_id, webhook_url)
    return "ok"


@app.post("/user-payment")
async def user_paymeny(paymeny_info: Payment):
    if paymeny_info.user_amount > paymeny_info.total_sale_amount:
        result = "ok"
    else:
        result = "error"

    notification_data = {
        "payment_status": result
    }

    webhook_urls = await get_webhook_urls()
    async with httpx.AsyncClient() as client:
        for webhook_url in webhook_urls:
            resp = await client.post(webhook_url, json=notification_data)
            if (resp.status_code != 200):
                print(f"Failed to send notification to {webhook_url}")
    return notification_data


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8001, reload=True)
