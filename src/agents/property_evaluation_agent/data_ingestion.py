import requests

RENTCAST_API_KEY = 'YOUR_RENTCAST_API_KEY'
ESTATED_API_KEY = 'YOUR_ESTATED_API_KEY'

def fetch_rentcast_data(address):
    url = f'https://api.rentcast.io/v1/properties?address={address}'
    headers = {'X-Api-Key': RENTCAST_API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"RentCast API error: {response.text}")

def fetch_estated_data(address):
    url = f'https://api.estated.com/property?token={ESTATED_API_KEY}&address={address}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Estated API error: {response.text}")
