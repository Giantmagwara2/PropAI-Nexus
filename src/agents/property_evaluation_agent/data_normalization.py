def normalize_data(rentcast_data, estated_data):
    # Normalize keys and map into a unified schema
    normalized = {
        'property_size': estated_data.get('data', {}).get('structure', {}).get('total_area', 0),
        'year_built': estated_data.get('data', {}).get('structure', {}).get('year_built', 0),
        'bedrooms': estated_data.get('data', {}).get('structure', {}).get('beds_count', 0),
        'bathrooms': estated_data.get('data', {}).get('structure', {}).get('baths', 0),
        'estimated_rent': rentcast_data.get('estimated_rent', {}).get('amount', 0),
        'neighborhood_rent_avg': rentcast_data.get('neighborhood', {}).get('rent', {}).get('average', 0)
    }
    return normalized
