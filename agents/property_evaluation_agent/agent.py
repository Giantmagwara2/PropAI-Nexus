# agents/property_evaluation_agent/agent.py

from data_ingestion import fetch_rentcast_data, fetch_estated_data
from data_normalization import normalize_data
from valuation_model import train_valuation_model, predict_property_value

class PropertyEvaluationAgent:
    def __init__(self):
        self.model = train_valuation_model()

    def evaluate(self, property_details):
        # Fetch data
        rentcast_data = fetch_rentcast_data(property_details['address'])
        estated_data = fetch_estated_data(property_details['address'])

        # Normalize and merge data
        combined_data = normalize_data(rentcast_data, estated_data)

        # Predict property value
        valuation = predict_property_value(self.model, combined_data)

        return {
            "valuation": valuation,
            "currency": "USD"  # To be localized later
        }
