# data_sources/attom.py

from utils.api_helpers import make_get_request
from config import API_KEYS, ENDPOINTS

def get_property_details_attom(address, postal_code):
    url = ENDPOINTS['attom'] + 'property/address'
    
    headers = {
        'apikey': API_KEYS['attom']
    }

    params = {
        'address1': address,
        'postalcode': postal_code
    }

    data = make_get_request(url, headers=headers, params=params)
    
    if data:
        # Process data as needed
        return data
    else:
        return {'error': 'No data found from ATTOM'}
