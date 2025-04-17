# /backend/routes/rental.py
from fastapi import APIRouter, Depends, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
from models.predictive_model import predict_rental_yield
from middleware.auth import verify_api_key
from localization import get_localized_message
from tasks import log_prediction

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
        predicted_yield = predict_rental_yield(features)

        # Background task to log prediction
        background_tasks.add_task(log_prediction, {
            "input": features,
            "output": predicted_yield
        })

        return {
            "predicted_rental_yield_percent": round(predicted_yield, 2)
        }
    
    except Exception as e:
        lang = request.headers.get("Accept-Language", "en").split(",")[0]
        message = get_localized_message(lang, 'internal_server_error')
        raise HTTPException(status_code=500, detail=message)
