from fastapi import Request, HTTPException
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "x-api-key"
API_KEY = "your-secure-api-key"  # Load from environment for production

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_api_key(request: Request):
    key = await api_key_header(request)
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
