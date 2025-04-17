# /backend/api/dashboard.py
from fastapi import APIRouter
from pydantic import BaseModel

# Sample data, replace with real DB/logic
class DashboardMetrics(BaseModel):
    total_properties: int
    total_estimated_value: float
    average_rental_yield: float
    active_predictions: int

router = APIRouter()

# Sample endpoint to get dashboard metrics
@router.get("/metrics", response_model=DashboardMetrics)
async def get_dashboard_metrics():
    # Replace with actual logic to fetch data from your database or services
    metrics = DashboardMetrics(
        total_properties=1240,
        total_estimated_value=48300000,
        average_rental_yield=6.4,
        active_predictions=89
    )
    return metrics
