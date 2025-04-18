# src/agents/smart_contract_agent/contract_handler.py

from .agent import SmartContractAgent
from .fiat_manager import handle_fiat_transaction
from .schemas import DealInput
from .utils import detect_payment_type

class ContractHandler:
    def __init__(self):
        self.smart_contract_agent = SmartContractAgent()

    def handle_deal(self, deal: DealInput):
        """
        Handle a property sale deal, either crypto or fiat
        """
        payment_type = detect_payment_type(deal.payment_method)

        if payment_type == 'crypto':
            # Handle crypto contract creation
            result = self.smart_contract_agent.create_property_sale_contract(
                property_details={"valuation": deal.price},
                buyer_address=deal.buyer_wallet,
                seller_address=deal.seller_wallet
            )
            return result
        elif payment_type == 'fiat':
            # Handle fiat transaction
            return handle_fiat_transaction(deal.dict())
        else:
            return {"error": "Unsupported payment method"}
