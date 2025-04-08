# data_sources/estated.py

from utils.api_helpers import make_get_request
from config import API_KEYS, ENDPOINTS

def get_property_details_estated(address, postal_code):
    url = ENDPOINTS['estated']
    
    params = {
        'token': API_KEYS['estated'],
        'address': f"{address}, {postal_code}"
    }

    data = make_get_request(url, params=params)
    
    if data:
        # Clean or process Estated response as necessary
        return data
    else:
        return {'error': 'No data found from Estated'}
