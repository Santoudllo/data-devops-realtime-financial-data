import requests
import json
from kafka import KafkaProducer

API_KEY = 'cpmsf59r01qtggb9pf50cpmsf59r01qtggb9pf5g'
STOCK_SYMBOL = 'AAPL'
KAFKA_TOPIC = 'stock-data'
KAFKA_BROKER = 'localhost:9092'

def fetch_stock_data():
    url = f'https://finnhub.io/api/v1/quote?symbol={STOCK_SYMBOL}&token={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def produce_messages():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    stock_data = fetch_stock_data()
    producer.send(KAFKA_TOPIC, stock_data)
    producer.flush()

if __name__ == "__main__":
    produce_messages()
