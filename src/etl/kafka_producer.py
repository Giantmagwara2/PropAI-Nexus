from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_property_data():
    # Code to fetch data from Zillow, Zoopla, etc.
    property_data = {
        'source': 'Zillow',
        'data': {...}
    }
    producer.send('property_data_topic', property_data)
