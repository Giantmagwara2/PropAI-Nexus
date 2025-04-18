# src/agents/smart_contract_agent/contract_templates.py

def generate_property_sale_contract(property_details, buyer_address, seller_address):
    property_price = int(property_details['valuation']) * (10**18)  # Assume ETH and wei conversion
    contract_template = f"""
    pragma solidity ^0.8.0;

    contract PropertySale {{
        address public seller = {seller_address};
        address public buyer = {buyer_address};
        uint public price = {property_price};

        function completeSale() public payable {{
            require(msg.sender == buyer, "Only buyer can complete sale");
            require(msg.value == price, "Incorrect payment");
            payable(seller).transfer(msg.value);
        }}
    }}
    """
    return contract_template
