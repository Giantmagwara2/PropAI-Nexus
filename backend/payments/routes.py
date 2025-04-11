from fastapi import APIRouter, HTTPException
import stripe

router = APIRouter()
stripe.api_key = "your_stripe_secret_key"

@router.post("/create-payment-intent/")
async def create_payment_intent():
    try:
        intent = stripe.PaymentIntent.create(
            amount=5000,  # amount in cents (e.g. $50)
            currency='usd',
            payment_method_types=['card']
        )
        return {"clientSecret": intent.client_secret}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
