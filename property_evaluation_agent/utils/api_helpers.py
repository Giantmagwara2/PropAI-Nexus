import requests
import logging

# Set up logging (you can adjust log level as needed)
logging.basicConfig(level=logging.ERROR, filename="api_errors.log", 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def make_get_request(url, headers=None, params=None, timeout=10):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        response.raise_for_status()  # Will raise an HTTPError if the status is 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API Request failed: {e}")
        return None
