# main.py

from data_sources.attom import get_property_details_attom
from data_sources.zoopla import search_properties_zoopla
from data_sources.estated import get_property_details_estated
from data_sources.rentcast import get_rental_data_rentcast
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.property_evaluation_agent import PropertyEvaluationAgent
from localization import get_localized_message

def evaluate_property(address, postal_code, area, city='', state='', zip_code='', language='en'):
    # Fetch property data from different sources
    print("Fetching data from ATTOM (US Market)...")
    attom_data = get_property_details_attom(address, postal_code)
    
    print("Fetching data from Estated (US Market)...")
    estated_data = get_property_details_estated(address, postal_code)
    
    print("Fetching rental data from RentCast (US Market)...")
    rentcast_data = get_rental_data_rentcast(address, city, state, zip_code)
    
    print("Fetching data from Zoopla (UK Market)...")
    zoopla_data = search_properties_zoopla(area)

    # Perform Market Analysis
    print("Running market analysis...")
    market_analysis_agent = MarketAnalysisAgent()
    market_trends = market_analysis_agent.fetch_market_data()
    
    # Perform Property Evaluation
    print("Running property evaluation...")
    property_evaluation_agent = PropertyEvaluationAgent()
    property_evaluation_report = property_evaluation_agent.evaluate_property_data(
        attom_data, estated_data, rentcast_data, zoopla_data
    )
    
    # Add market analysis data to the evaluation
    evaluation_report = {
        'property_evaluation': property_evaluation_report,
        'market_trends': market_trends
    }

    # Localization of the message (optional)
    localized_message = get_localized_message(language, 'internal_server_error')  # Example of using the localization system

    # Return the complete evaluation report
    return {
        'evaluation_report': evaluation_report,
        'localized_message': localized_message
    }

if __name__ == "__main__":
    # Example run - replace these values with actual inputs
    address = "123 Main St"
    postal_code = "90210"
    area = "London"
    city = "Los Angeles"
    state = "CA"
    zip_code = "90210"
    language = "en"  # Change language as needed

    report = evaluate_property(address, postal_code, area, city, state, zip_code, language)
    print("Complete Property Evaluation Report:")
    print(report)
