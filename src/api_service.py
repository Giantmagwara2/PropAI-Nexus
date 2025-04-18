# src/api_service.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# 🧠 Import Smart Contract Agent
from agents.smart_contract_agent.agent import SmartContractAgent

# Initialize app and agents
app = FastAPI()
model = joblib.load('property_value_model.pkl')
smart_contract_agent = SmartContractAgent()

# Request models
class Property(BaseModel):
    size: float
    bedrooms: int
    bathrooms: int
    location: str
    age: int

class ContractRequest(BaseModel):
    property_details: dict
    buyer_address: str
    seller_address: str

# Endpoints
@app.get("/")
async def root():
    return {"message": "Welcome to the AI Property Prediction and Smart Contract API!"}

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

@app.post("/create-contract/")
async def create_property_sale_contract(request: ContractRequest):
    """
    Create and deploy a smart contract for a property sale.
    """
    try:
        # Create property sale contract
        contract_info = smart_contract_agent.create_property_sale_contract(
            property_details=request.property_details,
            buyer_address=request.buyer_address,
            seller_address=request.seller_address
        )
        return {"message": "Contract deployed successfully", "contract_info": contract_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
