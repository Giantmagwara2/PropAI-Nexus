from typing import Dict, Any

class PropertyEvaluationAgent:
    def __init__(self):
        self.sources = {
            'Zillow': self.fetch_from_zillow,
            'Estated': self.fetch_from_estated,
            'RentCast': self.fetch_from_rentcast
        }

    def fetch_from_zillow(self, address: str) -> Dict[str, Any]:
        return {
            'zestimate': 320000,
            'bedrooms': 3,
            'bathrooms': 2,
            'square_feet': 1450
        }

    def fetch_from_estated(self, address: str) -> Dict[str, Any]:
        return {
            'market_value': 315000,
            'lot_size': 6000,
            'year_built': 1998
        }

    def fetch_from_rentcast(self, address: str) -> Dict[str, Any]:
        return {
            'monthly_rent': 1850,
            'rental_yield': 0.07
        }

    def normalize_and_merge(self, address: str) -> Dict[str, Any]:
        data = {}
        for source, fetcher in self.sources.items():
            data[source] = fetcher(address)

        evaluation = {
            'address': address,
            'estimated_value': (data['Zillow']['zestimate'] + data['Estated']['market_value']) / 2,
            'bedrooms': data['Zillow']['bedrooms'],
            'bathrooms': data['Zillow']['bathrooms'],
            'square_feet': data['Zillow']['square_feet'],
            'lot_size': data['Estated']['lot_size'],
            'year_built': data['Estated']['year_built'],
            'monthly_rent': data['RentCast']['monthly_rent'],
            'rental_yield': data['RentCast']['rental_yield']
        }

        return evaluation
