from fastapi import APIRouter, Depends, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
from models.predictive_model import predict_property_value
from middleware.auth import verify_api_key
from localization import get_localized_message
from tasks import log_prediction

router = APIRouter()

class PropertyRequest(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int
    country: str = "US"
    currency: str = "USD"

@router.post("/property", dependencies=[Depends(verify_api_key)])
async def property_prediction(
    property: PropertyRequest,
    request: Request,
    background_tasks: BackgroundTasks
):
    try:
        features = property.dict()
        predicted_value = predict_property_value(features)

        # Add logging in background
        background_tasks.add_task(log_prediction, {
            "input": features,
            "output": predicted_value
        })

        return {"predicted_value": predicted_value, "currency": property.currency}
    
    except Exception as e:
        lang = request.headers.get("Accept-Language", "en").split(",")[0]
        message = get_localized_message(lang, 'internal_server_error')
        raise HTTPException(status_code=500, detail=message)
