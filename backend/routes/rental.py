# /backend/routes/rental.py
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from models.predictive_model import predict_rental_yield
from localization import get_localized_message

router = APIRouter()

class PropertyInput(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int
    country: str = "US"
    currency: str = "USD"

@router.post("/")
async def rental_yield_prediction(property: PropertyInput, request: Request):
    try:
        result = predict_rental_yield(property)
        return result
    except Exception:
        lang = request.headers.get("Accept-Language", "en").split(",")[0]
        message = get_localized_message(lang, 'internal_server_error')
        raise HTTPException(status_code=500, detail=message)
