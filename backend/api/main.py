from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import locale
from forex_python.converter import CurrencyRates

app = FastAPI()

# Load trained property model
property_model = joblib.load('models/property_value_model.pkl')
rental_model = joblib.load('models/rental_yield_model.pkl')  # <- Ensure this model exists

# Currency converter
currency_converter = CurrencyRates()

# Base property input model
class Property(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int
    country: str = "US"
    currency: str = "USD"

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/predict/")
async def predict_property_value(property: Property):
    try:
        df = pd.DataFrame([property.dict()])
        df.drop(columns=["country", "currency"], inplace=True)

        df = pd.get_dummies(df)
        df = df.reindex(columns=property_model.feature_names_in_, fill_value=0)

        prediction = property_model.predict(df)[0]

        # Convert prediction to target currency
        if property.currency != "USD":
            prediction = currency_converter.convert("USD", property.currency, prediction)

        return {"predicted_price": round(prediction, 2), "currency": property.currency}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rental-yield/")
async def predict_rental_yield(property: Property):
    try:
        df = pd.DataFrame([property.dict()])
        df.drop(columns=["country", "currency"], inplace=True)

        df = pd.get_dummies(df)
        df = df.reindex(columns=rental_model.feature_names_in_, fill_value=0)

        prediction = rental_model.predict(df)[0]
        return {"predicted_rental_yield_percent": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
