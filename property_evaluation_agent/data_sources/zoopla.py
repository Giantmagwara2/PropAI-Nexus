# data_sources/zoopla.py

from utils.api_helpers import make_get_request
from config import API_KEYS, ENDPOINTS

def search_properties_zoopla(area, listing_status='sale'):
    url = ENDPOINTS['zoopla'] + 'property_listings.json'
    
    params = {
        'api_key': API_KEYS['zoopla'],
        'area': area,
        'listing_status': listing_status
    }

    data = make_get_request(url, params=params)
    
    if data:
        return data
    else:
        return {'error': 'No data found from Zoopla'}
