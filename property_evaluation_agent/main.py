# main.py

from data_sources.attom import get_property_details_attom
from data_sources.zoopla import search_properties_zoopla
from data_sources.estated import get_property_details_estated
from data_sources.rentcast import get_rental_data_rentcast

def evaluate_property(address, postal_code, area, city='', state='', zip_code=''):
    print("Fetching data from ATTOM (US Market)...")
    attom_data = get_property_details_attom(address, postal_code)
    
    print("Fetching data from Estated (US Market)...")
    estated_data = get_property_details_estated(address, postal_code)
    
    print("Fetching rental data from RentCast (US Market)...")
    rentcast_data = get_rental_data_rentcast(address, city, state, zip_code)
    
    print("Fetching data from Zoopla (UK Market)...")
    zoopla_data = search_properties_zoopla(area)
    
    evaluation_report = {
        'attom_data': attom_data,
        'estated_data': estated_data,
        'rentcast_data': rentcast_data,
        'zoopla_data': zoopla_data
    }
    
    return evaluation_report

if __name__ == "__main__":
    # Example run - you can replace these with actual values
    address = "123 Main St"
    postal_code = "90210"
    area = "London"
    city = "Los Angeles"
    state = "CA"
    zip_code = "90210"

    report = evaluate_property(address, postal_code, area, city, state, zip_code)
    print("Complete Property Evaluation Report:")
    print(report)
