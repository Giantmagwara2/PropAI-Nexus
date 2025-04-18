# src/agents/smart_contract_agent/agent.py

from web3 import Web3
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

class SmartContractAgent:
    def __init__(self):
        infura_url = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")
        private_key = os.getenv("WALLET_PRIVATE_KEY", "YOUR_PRIVATE_KEY")
        account_address = os.getenv("ACCOUNT_ADDRESS", "YOUR_WALLET_ADDRESS")
        chain_id = int(os.getenv("CHAIN_ID", 1))  # Default to Ethereum Mainnet

        # Initialize Web3 connection
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        self.private_key = private_key
        self.account_address = account_address
        self.chain_id = chain_id

        # Verify Ethereum connection
        if not self.web3.is_connected():
            raise Exception("Failed to connect to Ethereum network. Please check your INFURA_URL.")

    def create_property_sale_contract(self, property_details, buyer_address, seller_address):
        """
        Deploy a smart contract for a property sale on Ethereum blockchain.
        """
        try:
            valuation = property_details.get('valuation')
            if valuation is None:
                raise ValueError("Property valuation must be provided in property_details.")

            # Generate Solidity source dynamically
            contract_source_code = self._generate_contract_source(valuation, buyer_address, seller_address)

            # Mock compile the contract (replace with real compilation when ready)
            compiled_contract = self._mock_compile(contract_source_code)

            # Create contract instance
            PropertySaleContract = self.web3.eth.contract(abi=compiled_contract['abi'], bytecode=compiled_contract['bytecode'])

            # Build transaction
            nonce = self.web3.eth.get_transaction_count(self.account_address)
            transaction = PropertySaleContract.constructor(
                valuation, buyer_address, seller_address
            ).build_transaction({
                'chainId': self.chain_id,
                'gas': 3000000,
                'gasPrice': self.web3.to_wei('50', 'gwei'),
                'nonce': nonce,
            })

            # Sign transaction
            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)

            # Send transaction
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)

            return {
                "transaction_hash": self.web3.to_hex(tx_hash),
                "message": "Smart contract deployed successfully."
            }
        except Exception as e:
            raise Exception(f"Smart contract deployment failed: {str(e)}")

    def _generate_contract_source(self, valuation, buyer, seller):
        """
        Dynamically generate Solidity smart contract source code.
        """
        return f"""
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.0;

        contract PropertySale {{
            uint256 public valuation;
            address public buyer;
            address public seller;

            constructor(uint256 _valuation, address _buyer, address _seller) {{
                valuation = _valuation;
                buyer = _buyer;
                seller = _seller;
            }}
        }}
        """

    def _mock_compile(self, source_code):
        """
        Mock compilation of Solidity contract.
        In production, replace this with real solcx.compile_source(source_code).
        """
        abi = [
            {
                "inputs": [
                    {"internalType": "uint256", "name": "_valuation", "type": "uint256"},
                    {"internalType": "address", "name": "_buyer", "type": "address"},
                    {"internalType": "address", "name": "_seller", "type": "address"},
                ],
                "stateMutability": "nonpayable",
                "type": "constructor",
            },
            {
                "inputs": [],
                "name": "valuation",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "view",
                "type": "function",
            },
            {
                "inputs": [],
                "name": "buyer",
                "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                "stateMutability": "view",
                "type": "function",
            },
            {
                "inputs": [],
                "name": "seller",
                "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                "stateMutability": "view",
                "type": "function",
            }
        ]
        bytecode = '0x608060405234801561001057600080fd5b506...'  # (Mocked bytecode here)
        return {"abi": abi, "bytecode": bytecode}
