# /backend/main.py
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import joblib
import pandas as pd
import httpx

# Import middleware, localization, and routers
from middleware.auth import verify_api_key
from localization import get_localized_message
from payments.stripe_payment import stripe_router

# Initialize FastAPI app
app = FastAPI()

# Include payment router
app.include_router(stripe_router, prefix="/api/payments")

# Load trained models
property_model = joblib.load('models/property_value_model.pkl')
rental_model = joblib.load('models/rental_yield_model.pkl')

# Define request schema
class Property(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int
    country: str = "US"
    currency: str = "USD"

# Global exception handler for internationalized error responses
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    lang = request.headers.get("Accept-Language", "en").split(",")[0]
    message = get_localized_message(lang, 'internal_server_error')
    return JSONResponse(status_code=500, content={"detail": message})

# Predict property price
@app.post("/predict/", dependencies=[Depends(verify_api_key)])
async def predict_property_value(property: Property, request: Request):
    try:
        df = pd.DataFrame([property.dict()])
        df.drop(columns=["country", "currency"], inplace=True)
        df = pd.get_dummies(df)
        df = df.reindex(columns=property_model.feature_names_in_, fill_value=0)
        prediction = property_model.predict(df)[0]

        # Currency conversion
        base_currency = "USD"
        target_currency = property.currency.upper()
        if target_currency != base_currency:
            url = f"https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={prediction}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                data = response.json()
                converted_price = data["result"]
        else:
            converted_price = prediction

        return {
            "predicted_price": round(converted_price, 2),
            "currency": target_currency
        }
    except Exception as e:
        lang = request.headers.get("Accept-Language", "en").split(",")[0]
        message = get_localized_message(lang, 'internal_server_error')
        raise HTTPException(status_code=500, detail=message)

# Predict rental yield
@app.post("/rental-yield/", dependencies=[Depends(verify_api_key)])
async def predict_rental_yield(property: Property, request: Request):
    try:
        df = pd.DataFrame([property.dict()])
        df.drop(columns=["country", "currency"], inplace=True)
        df = pd.get_dummies(df)
        df = df.reindex(columns=rental_model.feature_names_in_, fill_value=0)
        prediction = rental_model.predict(df)[0]
        return {"predicted_rental_yield_percent": round(prediction, 2)}
    except Exception as e:
        lang = request.headers.get("Accept-Language", "en").split(",")[0]
        message = get_localized_message(lang, 'internal_server_error')
        raise HTTPException(status_code=500, detail=message)
