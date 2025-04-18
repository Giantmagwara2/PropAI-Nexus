# src/agents/smart_contract_agent/agent.py

from contract_manager import deploy_contract
from contract_templates import generate_property_sale_contract

class SmartContractAgent:
    def __init__(self, blockchain='ethereum'):
        self.blockchain = blockchain

    def create_property_sale_contract(self, property_details, buyer_address, seller_address):
        contract_code = generate_property_sale_contract(property_details, buyer_address, seller_address)
        contract_address = deploy_contract(contract_code)
        return {
            "contract_address": contract_address,
            "blockchain": self.blockchain
        }

    # Future: create_rental_agreement(), fractional_ownership_token(), etc.

