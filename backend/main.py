# /backend/main.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middleware.auth import verify_api_key
from localization import get_localized_message

from payments.stripe_payment import stripe_router
from backend.api.routes.prediction import router as prediction_router
from routes.rental import router as rental_router

# Initialize FastAPI app
app = FastAPI(
    title="PropAI Nexus API",
    description="An AI-driven real estate prediction platform",
    version="1.0.0"
)

# Include Routers
app.include_router(stripe_router, prefix="/api/payments")
app.include_router(prediction_router, prefix="/api/predictions", tags=["Predictions"])
app.include_router(rental_router, prefix="/api/rental", tags=["Rental Yield"])

# Global Exception Handler for Internationalized Errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    lang = request.headers.get("Accept-Language", "en").split(",")[0]
    message = get_localized_message(lang, 'internal_server_error')
    return JSONResponse(
        status_code=500,
        content={"detail": message}
    )
