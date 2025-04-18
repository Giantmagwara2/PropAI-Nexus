# src/agents/smart_contract_agent/contract_manager.py

from .blockchain_connector import compile_and_deploy_contract

def deploy_contract(solidity_code):
    """
    Deploys compiled Solidity code to Ethereum and returns contract address.
    """
    contract_address = compile_and_deploy_contract(solidity_code)
    return contract_address
