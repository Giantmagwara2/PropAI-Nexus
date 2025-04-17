# /backend/routes/metrics.py

from fastapi import APIRouter, Depends, HTTPException, Request
from backend.models.metrics_agent import MetricsAgent
from middleware.auth import verify_api_key
from localization import get_localized_message

router = APIRouter()

# Create global metrics agent
metrics_agent = MetricsAgent()

@router.get("/dashboard/metrics", dependencies=[Depends(verify_api_key)])
async def get_dashboard_metrics(request: Request):
    try:
        return metrics_agent.get_metrics()
    except Exception:
        lang = request.headers.get("Accept-Language", "en").split(",")[0]
        message = get_localized_message(lang, 'internal_server_error')
        raise HTTPException(status_code=500, detail=message)
