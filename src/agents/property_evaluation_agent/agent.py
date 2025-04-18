# agents/property_evaluation_agent/agent.py

from data_ingestion import fetch_rentcast_data, fetch_estated_data
from data_normalization import normalize_data
from valuation_model import train_valuation_model, predict_property_value

class PropertyEvaluationAgent:
    def __init__(self):
        # Initialize the model
        self.model = train_valuation_model()

    def evaluate(self, property_details):
        # Step 1: Fetch Data
        print("Fetching RentCast data...")
        rentcast_data = fetch_rentcast_data(property_details['address'])

        print("Fetching Estated data...")
        estated_data = fetch_estated_data(property_details['address'])

        # Step 2: Normalize Data
        print("Normalizing data...")
        combined_data = normalize_data(rentcast_data, estated_data)

        # Step 3: Predict Property Value
        print("Predicting property value...")
        valuation = predict_property_value(self.model, combined_data)

        # Return a comprehensive evaluation report
        evaluation_report = {
            "valuation": valuation,
            "currency": "USD",  # This can later be localized
            "property_details": property_details,
            "data_sources": {
                "rentcast": rentcast_data,
                "estated": estated_data
            }
        }
        return evaluation_report

if __name__ == "__main__":
    # Test the agent with an example property
    agent = PropertyEvaluationAgent()

    property_details = {
        'address': '123 Main St, Los Angeles, CA, 90210',
        'postal_code': '90210',
        'city': 'Los Angeles',
        'state': 'CA',
        'zip_code': '90210'
    }

    report = agent.evaluate(property_details)
    print("Property Evaluation Report:")
    print(report)
