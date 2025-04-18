# /src/services/data_merger_service.py

from typing import Optional, Dict, Any

class DataMergerService:
    def __init__(self):
        pass

    async def normalize_attom_data(self, attom_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {
                'property_value': attom_data.get('price', 0),
                'bed_count': attom_data.get('bedrooms', 0),
                'bath_count': attom_data.get('bathrooms', 0),
                'area_sqft': attom_data.get('sqft', 0),
            }
        except Exception as e:
            print(f"Normalization failed for ATTOM: {e}")
            return {}

    async def normalize_estated_data(self, estated_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {
                'property_value_estated': estated_data.get('valuation', 0),
                'year_built': estated_data.get('year_built', 0),
            }
        except Exception as e:
            print(f"Normalization failed for Estated: {e}")
            return {}

    async def normalize_rentcast_data(self, rentcast_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {
                'predicted_rental_yield': rentcast_data.get('rental_yield', 0),
            }
        except Exception as e:
            print(f"Normalization failed for Rentcast: {e}")
            return {}

    async def normalize_zoopla_data(self, zoopla_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return {
                'property_value_zoopla': zoopla_data.get('estimated_price', 0),
                'property_type': zoopla_data.get('property_type', 'Unknown'),
            }
        except Exception as e:
            print(f"Normalization failed for Zoopla: {e}")
            return {}

    async def merge_property_data(
        self,
        attom_data: Optional[Dict[str, Any]] = None,
        estated_data: Optional[Dict[str, Any]] = None,
        rentcast_data: Optional[Dict[str, Any]] = None,
        zoopla_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        normalized_data = {}

        if attom_data:
            normalized_data.update(await self.normalize_attom_data(attom_data))
        if estated_data:
            normalized_data.update(await self.normalize_estated_data(estated_data))
        if rentcast_data:
            normalized_data.update(await self.normalize_rentcast_data(rentcast_data))
        if zoopla_data:
            normalized_data.update(await self.normalize_zoopla_data(zoopla_data))

        # Merge property values
        property_values = [
            normalized_data.get('property_value', 0),
            normalized_data.get('property_value_estated', 0),
            normalized_data.get('property_value_zoopla', 0)
        ]
        property_values = [v for v in property_values if v > 0]

        normalized_data['average_property_value'] = (
            sum(property_values) / len(property_values) if property_values else None
        )

        return normalized_data
