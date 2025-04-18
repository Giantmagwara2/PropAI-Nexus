# src/agents/smart_contract_agent/utils.py

def detect_payment_type(payment_method: str) -> str:
    """
    Detects if the payment method is crypto or fiat
    """
    if payment_method.lower() in ['eth', 'usdc', 'crypto']:
        return 'crypto'
    elif payment_method.lower() in ['usd', 'eur', 'fiat']:
        return 'fiat'
    else:
        return 'unknown'
