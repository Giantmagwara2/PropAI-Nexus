# data_sources/rentcast.py

from utils.api_helpers import make_get_request
from config import API_KEYS, ENDPOINTS

def get_rental_data_rentcast(address, city, state, zip_code):
    url = ENDPOINTS['rentcast'] + 'rental-analysis'
    
    headers = {
        'X-Api-Key': API_KEYS['rentcast']
    }

    params = {
        'address': address,
        'city': city,
        'state': state,
        'zip_code': zip_code
    }

    data = make_get_request(url, headers=headers, params=params)
    
    if data:
        return data
    else:
        return {'error': 'No rental data found from RentCast'}
