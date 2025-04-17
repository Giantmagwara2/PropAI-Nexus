# /backend/main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from middleware.auth import verify_api_key
from localization import get_localized_message
from payments.stripe_payment import stripe_router
from routes.prediction import router as prediction_router
from routes.rental import router as rental_router

import joblib

# Initialize FastAPI app
app = FastAPI()

# Load models globally (can be used inside other routers if needed)
property_model = joblib.load('models/property_value_model.pkl')
rental_model = joblib.load('models/rental_yield_model.pkl')

# Include routers
app.include_router(stripe_router, prefix="/api/payments")
app.include_router(prediction_router, prefix="/api/predictions")
app.include_router(rental_router, prefix="/api/rental")

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    lang = request.headers.get("Accept-Language", "en").split(",")[0]
    message = get_localized_message(lang, 'internal_server_error')
    return JSONResponse(status_code=500, content={"detail": message})
