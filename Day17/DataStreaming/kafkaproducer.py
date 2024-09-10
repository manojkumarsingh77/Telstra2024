from kafka import KafkaProducer
import json
import time
import random

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Generate mock telecom data
def generate_telecom_data():
    sample_data = {
        "user_id": random.randint(1000, 9999),
        "call_duration": random.randint(1, 500),  # in seconds
        "data_usage": round(random.uniform(0.1, 10.0), 2),  # in GB
        "location": random.choice(["New York", "California", "Texas", "Florida"]),
        "call_type": random.choice(["local", "international", "roaming"]),
        "timestamp": time.time()
    }
    return sample_data

# Continuously send data to Kafka
if __name__ == "__main__":
    while True:
        data = generate_telecom_data()
        producer.send('telecom-data', value=data)
        print(f"Sent: {data}")
        time.sleep(1)  # Sleep for a second before sending the next record
