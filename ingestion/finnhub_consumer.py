from kafka import KafkaConsumer
import json

KAFKA_TOPIC = 'stock-data'
KAFKA_BROKER = 'localhost:9092'

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f"Received message: {message.value}")
