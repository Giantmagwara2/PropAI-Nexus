# src/api_service.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# 🧠 Import Agents
from agents.smart_contract_agent.agent import SmartContractAgent
from agents.upgrade_manager.agent import UpgradeManagerAgent
from agents.performance_monitor.agent import PerformanceMonitorAgent
from agents.self_training.gnn_autoupdate_agent import GNNUpdateAgent

# Initialize app and agents
app = FastAPI()

# Load ML model
model = joblib.load('property_value_model.pkl')

# Initialize agents
smart_contract_agent = SmartContractAgent()
upgrade_manager = UpgradeManagerAgent()
performance_monitor = PerformanceMonitorAgent()
gnn_update_agent = GNNUpdateAgent()

# 📦 Request Models
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

# 🚀 Endpoints
@app.get("/")
async def root():
    return {"message": "🏡 Welcome to the PropAI Nexus: AI Property + Smart Contract + Self-Evolving System!"}

@app.post("/predict/")
async def predict_property_value(property: Property):
    """
    Predict property value using the trained machine learning model.
    """
    try:
        # Prepare input data
        input_data = pd.DataFrame([property.dict()])
        input_data = pd.get_dummies(input_data)

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
    Create and deploy a smart contract for a property sale transaction.
    """
    try:
        contract_info = smart_contract_agent.create_property_sale_contract(
            property_details=request.property_details,
            buyer_address=request.buyer_address,
            seller_address=request.seller_address
        )
        return {"message": "📜 Smart contract deployed successfully.", "contract_info": contract_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/check-upgrades/")
async def check_for_upgrades():
    """
    Check for available AI library/model upgrades.
    """
    try:
        upgrade_manager.check_for_updates()
        return {"message": "🔍 Checked for available upgrades."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/trigger-upgrades/")
async def upgrade_all_packages():
    """
    Automatically upgrade all major AI and system packages.
    """
    try:
        upgrade_manager.upgrade_all()
        return {"message": "⬆️ All core packages upgraded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/monitor-performance/")
async def monitor_performance():
    """
    Collect system performance metrics and push them to Redis.
    """
    try:
        performance_monitor.push_metrics_to_redis()
        return {"message": "📈 Performance metrics collected and pushed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/retrain-gnn/")
async def retrain_gnn_model():
    """
    Retrain the GNN (Graph Neural Network) model automatically.
    """
    try:
        # Import dummy data for now; replace with real data loading later
        from torch_geometric.data import Data
        dummy_data = Data()
        gnn_update_agent.retrain_gnn(dummy_data)
        return {"message": "♻️ GNN retraining triggered successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
