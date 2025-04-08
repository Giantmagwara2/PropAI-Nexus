# src/data_merger.py

def normalize_attom_data(attom_data):
    # Example: Normalize ATTOM data keys
    return {
        'property_value': attom_data.get('price'),
        'bed_count': attom_data.get('bedrooms'),
        'bath_count': attom_data.get('bathrooms'),
        'area_sqft': attom_data.get('sqft')
    }

def normalize_estated_data(estated_data):
    # Example: Normalize Estated data keys
    return {
        'property_value_estated': estated_data.get('valuation'),
        'year_built': estated_data.get('year_built')
    }

def normalize_rentcast_data(rentcast_data):
    # Example: Normalize RentCast data
    return {
        'predicted_rental_yield': rentcast_data.get('rental_yield')
    }

def normalize_zoopla_data(zoopla_data):
    # Example: Normalize Zoopla data keys
    return {
        'property_value_zoopla': zoopla_data.get('estimated_price'),
        'property_type': zoopla_data.get('property_type')
    }

def merge_property_data(attom_data, estated_data, rentcast_data, zoopla_data):
    """
    Merge normalized data from various sources into a unified evaluation report.
    """
    normalized_data = {}
    normalized_data.update(normalize_attom_data(attom_data))
    normalized_data.update(normalize_estated_data(estated_data))
    normalized_data.update(normalize_rentcast_data(rentcast_data))
    normalized_data.update(normalize_zoopla_data(zoopla_data))
    
    # Merge property values from multiple sources
    property_values = []
    if normalized_data.get('property_value'):
        property_values.append(normalized_data['property_value'])
    if normalized_data.get('property_value_estated'):
        property_values.append(normalized_data['property_value_estated'])
    if normalized_data.get('property_value_zoopla'):
        property_values.append(normalized_data['property_value_zoopla'])
    
    if property_values:
        normalized_data['average_property_value'] = sum(property_values) / len(property_values)
    else:
        normalized_data['average_property_value'] = None

    return normalized_data

# For testing purposes
if __name__ == '__main__':
    attom_data = {'price': 500000, 'bedrooms': 3, 'bathrooms': 2, 'sqft': 1500}
    estated_data = {'valuation': 520000, 'year_built': 1990}
    rentcast_data = {'rental_yield': 0.06}  # 6%
    zoopla_data = {'estimated_price': 510000, 'property_type': 'Condo'}

    merged_data = merge_property_data(attom_data, estated_data, rentcast_data, zoopla_data)
    print("Unified Property Evaluation Report:")
    print(merged_data)
