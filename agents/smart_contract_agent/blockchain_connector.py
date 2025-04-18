# src/agents/smart_contract_agent/blockchain_connector.py

from web3 import Web3
import solcx

# Connect to Ethereum (Local Ganache / Infura / Alchemy)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Change later to mainnet or Infura endpoint

def compile_and_deploy_contract(solidity_code):
    """
    Compiles and deploys Solidity contract to Ethereum blockchain.
    """
    solcx.install_solc('0.8.0')
    compiled_sol = solcx.compile_source(
        solidity_code,
        output_values=['abi', 'bin']
    )

    contract_id, contract_interface = compiled_sol.popitem()
    abi = contract_interface['abi']
    bytecode = contract_interface['bin']

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    acct = w3.eth.accounts[0]
    tx_hash = contract.constructor().transact({'from': acct, 'gas': 3000000})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_receipt.contractAddress
