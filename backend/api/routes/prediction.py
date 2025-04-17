# /backend/routes/prediction.py

from fastapi import APIRouter, Depends, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
from backend.models.property_evaluator import PropertyEvaluatorAgent
from middleware.auth import verify_api_key
from localization import get_localized_message
from tasks import log_prediction

import joblib

# Load model and setup agent
model = joblib.load('property_value_model.pkl')
property_agent = PropertyEvaluatorAgent(model)

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

        # Use agent to predict
        predicted_price = property_agent.predict(features)

        result = {
            "predicted_price": predicted_price,
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
