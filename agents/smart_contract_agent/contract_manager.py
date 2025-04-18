# src/agents/smart_contract_agent/contract_manager.py

from blockchain_connector import compile_and_deploy

def deploy_contract(solidity_code):
    contract_address = compile_and_deploy(solidity_code)
    return contract_address
