!pip install kafka-python pandas




import random
import time
from kafka import KafkaProducer
import json
import pandas as pd
from datetime import datetime

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers=['<your-public-ip>:9092'],  # Replace with your Kafka broker's public IP
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# List of customer IDs (in real life, you would pull this from a database)
customers = [
    {'CustomerID': 'b019d218-4f18-4ea1-8c15-93f72b05df72', 'DeviceID': 1001},
    {'CustomerID': '377ddade-8e97-47b6-8e58-547ef7a8c50a', 'DeviceID': 1002},
    {'CustomerID': 'a6c49b54-6b14-46cf-955b-42f4b8e6bf7d', 'DeviceID': 1003},
]

# Function to generate network performance data with variability
def generate_network_performance_data(customer):
    signal_strength = random.uniform(50, 100)
    call_drop_rate = random.uniform(0, 5)
    data_transfer_speed = random.uniform(10, 100)
    
    # Add variability: If signal strength is low, reduce data transfer speed and increase call drop rate
    if signal_strength < 70:
        data_transfer_speed -= random.uniform(5, 15)
        call_drop_rate += random.uniform(1, 3)

    # Ensure values are within realistic ranges
    call_drop_rate = max(min(call_drop_rate, 10), 0)
    data_transfer_speed = max(data_transfer_speed, 5)
    
    data = {
        'DeviceID': customer['DeviceID'],
        'CustomerID': customer['CustomerID'],
        'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'SignalStrength': round(signal_strength, 2),  # Signal strength in dBm
        'CallDropRate': round(call_drop_rate, 2),  # Call drop rate percentage
        'DataTransferSpeed': round(data_transfer_speed, 2)  # Data transfer speed in Mbps
    }
    return data

# Function to generate customer complaints with correlation to network performance
def generate_complaint_data(customer, network_data):
    # Increase likelihood of complaints when signal strength is low or call drop rate is high
    complaint_probability = (5 - network_data['SignalStrength'] / 20) + (network_data['CallDropRate'] / 2)
    if random.random() < min(complaint_probability, 0.8):  # Complaints are more likely when network is poor
        data = {
            'CustomerID': customer['CustomerID'],
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'ComplaintType': random.choice(['Network Issue', 'Billing Dispute', 'Technical Support']),
            'ResolutionTime': random.randint(1, 5),  # Time in hours to resolve the complaint
            'SatisfactionRating': random.randint(1, 5)  # Satisfaction rating from 1 to 5
        }
        return data
    else:
        return None

# Function to send data to Kafka topic
def send_data_to_kafka():
    while True:
        for customer in customers:
            # Generate network performance data
            network_data = generate_network_performance_data(customer)
            print(f"Sending network performance data: {network_data}")
            producer.send('test1', value=network_data)
            
            # Generate correlated customer complaints
            complaint_data = generate_complaint_data(customer, network_data)
            if complaint_data:
                print(f"Sending complaint data: {complaint_data}")
                producer.send('test1', value=complaint_data)
            
            # Make sure Kafka sends the data immediately
            producer.flush()
        
        time.sleep(5)  # Sleep for 5 seconds before sending the next batch of data

# Start generating and sending streaming data to Kafka
send_data_to_kafka()
