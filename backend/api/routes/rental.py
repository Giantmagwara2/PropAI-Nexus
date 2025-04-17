# /backend/routes/rental.py

from fastapi import APIRouter, Depends, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
from backend.models.rental_yield_agent import RentalYieldAgent
from middleware.auth import verify_api_key
from localization import get_localized_message
from tasks import log_prediction

import joblib

# Load model and setup agent
model = joblib.load('rental_yield_model.pkl')
rental_agent = RentalYieldAgent(model)

router = APIRouter()

class RentalRequest(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int
    country: str = "US"
    currency: str = "USD"

@router.post("/rental-yield", dependencies=[Depends(verify_api_key)])
async def rental_yield_prediction(
    property: RentalRequest,
    request: Request,
    background_tasks: BackgroundTasks
):
    try:
        features = property.dict()

        # Predict rental yield using agent
        predicted_yield = rental_agent.predict(features)

        result = {
            "predicted_rental_yield_percent": round(predicted_yield, 2),
            "currency": features.get("currency", "USD"),
            "country": features.get("country", "US")
        }

        # Background logging
        background_tasks.add_task(log_prediction, {
            "input": features,
            "output": result
        })

        return result

    except Exception:
        lang = request.headers.get("Accept-Language", "en").split(",")[0]
        message = get_localized_message(lang, 'internal_server_error')
        raise HTTPException(status_code=500, detail=message)
