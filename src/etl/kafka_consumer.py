from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'property_data_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    property_data = message.value
    # Store data to your DB here
