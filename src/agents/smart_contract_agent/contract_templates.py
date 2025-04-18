# src/agents/smart_contract_agent/contract_templates.py

def generate_property_sale_contract(property_details, buyer_address, seller_address):
    """
    Dynamically generates a Solidity smart contract for a property sale.
    """
    property_price = int(property_details['valuation']) * (10**18)  # Convert to wei (1 ETH = 10^18 wei)
    buyer_address = f'"{buyer_address}"'
    seller_address = f'"{seller_address}"'

    contract_template = f"""
    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.0;

    contract PropertySale {{
        address public seller = {seller_address};
        address public buyer = {buyer_address};
        uint256 public price = {property_price};

        constructor() {{}}

        function completeSale() public payable {{
            require(msg.sender == buyer, "Only buyer can complete the sale");
            require(msg.value == price, "Incorrect payment amount");
            payable(seller).transfer(msg.value);
        }}
    }}
    """
    return contract_template
