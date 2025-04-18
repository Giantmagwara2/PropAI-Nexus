# src/agents/smart_contract_agent/blockchain_connector.py

from web3 import Web3
import solcx

# Connect to local Ganache or Infura endpoint
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

def compile_and_deploy(solidity_code):
    solcx.install_solc('0.8.0')
    compiled_sol = solcx.compile_source(solidity_code)
    contract_id, contract_interface = compiled_sol.popitem()
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    
    acct = w3.eth.accounts[0]
    tx_hash = contract.constructor().transact({'from': acct})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    return tx_receipt.contractAddress
