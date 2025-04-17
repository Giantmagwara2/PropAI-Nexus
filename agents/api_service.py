# src/api_service.py

from fastapi import FastAPI
import xgboost as xgb
import pandas as pd
import uvicorn

app = FastAPI()
MODEL_PATH = 'property_value_predictor.json'

# Load trained model
model = xgb.XGBRegressor()
model.load_model(MODEL_PATH)

@app.get("/")
def root():
    return {"message": "Welcome to the AI Property Prediction API!"}

@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"predicted_price": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
