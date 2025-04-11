from fastapi import Depends
from middleware.auth import verify_api_key

@app.post("/predict/", dependencies=[Depends(verify_api_key)])
async def predict_property_value(property: Property):
    ...
