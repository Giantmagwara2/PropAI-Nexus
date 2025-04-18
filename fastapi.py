# fastapi.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from agents.smart_contract_agent.agent import SmartContractAgent

app = FastAPI()

# Load the trained model
model = joblib.load('property_value_model.pkl')

# Initialize Smart Contract Agent
smart_contract_agent = SmartContractAgent()

# Define request bodies
class Property(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int

class DeployRequest(BaseModel):
    property_id: str  # We will use Redis to fetch based on property_id

# Endpoint for predicting property value
@app.post("/predict/")
async def predict_property_value(property: Property):
    try:
        input_data = pd.DataFrame([property.dict()])
        input_data = pd.get_dummies(input_data)
        model_features = model.feature_names_in_
        input_data = input_data.reindex(columns=model_features, fill_value=0)

        prediction = model.predict(input_data)
        return {"predicted_price": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# NEW ENDPOINT: Deploy smart contract for a property transaction
@app.post("/deploy_contract/")
async def deploy_contract(req: DeployRequest):
    try:
        result = smart_contract_agent.process_and_deploy(req.property_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
