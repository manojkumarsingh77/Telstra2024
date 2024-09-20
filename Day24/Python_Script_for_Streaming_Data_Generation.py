!pip install kafka-python pandas


import random
from datetime import datetime
import time
from kafka import KafkaProducer
import json
import uuid

# Function to generate random network performance data
def generate_network_performance_data():
    device_id = f"Router-{random.randint(1, 10)}"  # Automatically generate a random DeviceID (Router-1 to Router-10)
    customer_id = str(uuid.uuid4())  # Generate a random unique CustomerID
    
    signal_strength = random.uniform(50, 100)
    call_drop_rate = random.uniform(0, 5)
    data_transfer_speed = random.uniform(10, 100)
    
    # Correlate lower signal strength with higher call drop rates and slower data speeds
    if signal_strength < 70:
        data_transfer_speed -= random.uniform(5, 15)
        call_drop_rate += random.uniform(1, 3)
    
    # Ensure valid data range
    call_drop_rate = max(min(call_drop_rate, 10), 0)
    data_transfer_speed = max(data_transfer_speed, 5)
    
    data = {
        'DeviceID': device_id,
        'CustomerID': customer_id,
        'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'SignalStrength': round(signal_strength, 2),
        'CallDropRate': round(call_drop_rate, 2),
        'DataTransferSpeed': round(data_transfer_speed, 2)
    }
    return data

# Function to generate random customer complaints data
def generate_complaint_data(network_data):
    customer_id = network_data['CustomerID']
    
    # Increased chance of complaints if signal strength is low or call drop rate is high
    complaint_probability = (70 - network_data['SignalStrength']) / 100 + network_data['CallDropRate'] / 10
    if random.random() < complaint_probability:
        data = {
            'CustomerID': customer_id,
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'ComplaintType': random.choice(['Network Issue', 'Billing Dispute', 'Technical Support']),
            'ResolutionTime': random.randint(1, 5),  # Time in hours to resolve the complaint
            'SatisfactionRating': random.randint(1, 5)  # Rating from 1 to 5
        }
        return data
    return None

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Update with your Kafka server details
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to send data to Kafka topic
def send_data_to_kafka():
    while True:
        # Generate and send network performance data
        network_data = generate_network_performance_data()
        print(f"Sending network performance data: {network_data}")
        producer.send('network_performance', value=network_data)
        
        # Generate and send customer complaints based on network performance
        complaint_data = generate_complaint_data(network_data)
        if complaint_data:
            print(f"Sending complaint data: {complaint_data}")
            producer.send('customer_complaints', value=complaint_data)
        
        producer.flush()  # Ensure all messages are sent
        
        time.sleep(10)  # Sleep for 10 seconds before sending the next batch of data

# Start generating streaming data
if __name__ == "__main__":
    send_data_to_kafka()

