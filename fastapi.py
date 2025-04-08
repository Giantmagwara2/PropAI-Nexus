from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model
model = joblib.load('property_value_model.pkl')

# Define the request body
class Property(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int

# Endpoint for predicting property value
@app.post("/predict/")
async def predict_property_value(property: Property):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([property.dict()])

        # One-hot encode the input data to match training data
        input_data = pd.get_dummies(input_data)

        # Align input data with the model's expected input
        model_features = model.feature_names_in_
        input_data = input_data.reindex(columns=model_features, fill_value=0)

        # Make prediction
        prediction = model.predict(input_data)
        return {"predicted_price": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
