# src/agents/smart_contract_agent/schemas.py

from pydantic import BaseModel

class DealInput(BaseModel):
    property_id: str
    buyer_name: str
    buyer_wallet: str = None
    seller_wallet: str = None
    price: float
    currency: str
    payment_method: str
    payment_method_id: str = None  # For fiat deals
