import stripe
from fastapi import APIRouter, HTTPException

stripe.api_key = "your_stripe_secret_key"  # Load this from environment variables for production

stripe_router = APIRouter()

class PaymentRequest(BaseModel):
    amount: int  # Amount in cents
    currency: str = "usd"
    description: str

@stripe_router.post("/create-checkout-session/")
async def create_checkout_session(payment: PaymentRequest):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": payment.currency,
                        "product_data": {
                            "name": payment.description,
                        },
                        "unit_amount": payment.amount,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="https://yourdomain.com/success",
            cancel_url="https://yourdomain.com/cancel",
        )
        return {"id": session.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
