import requests
import random
import time
from datetime import datetime

# API URL for the Power BI streaming dataset (Replace with your actual URL)
power_bi_url = 'https://api.powerbi.com/beta/your_workspace_id/datasets/your_dataset_id/rows?key=your_api_key'

# Function to generate random telecom data for regions
def generate_telecom_data():
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    data = []

    for city in cities:
        signal_strength = round(random.uniform(1.0, 5.0), 2)  # Random signal strength between 1 and 5
        call_drop_rate = round(random.uniform(0, 0.2), 2)     # Random call drop rate between 0 and 0.2
        data_usage = random.randint(500, 5000)                # Random data usage in MB
        satisfaction_score = round(random.uniform(1, 5), 2)   # Random customer satisfaction score
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp

        data.append({
            'Timestamp': timestamp,
            'City': city,
            'SignalStrength': signal_strength,
            'CallDropRate': call_drop_rate,
            'DataUsageMB': data_usage,
            'CustomerSatisfaction': satisfaction_score
        })
    
    return data

# Function to push data to Power BI Streaming Dataset
def push_data_to_power_bi():
    while True:
        # Generate new telecom data
        data = generate_telecom_data()

        # Send the data to Power BI Streaming Dataset
        response = requests.post(power_bi_url, json=data)

        if response.status_code == 200:
            print("Data sent successfully to Power BI!")
        else:
            print(f"Failed to send data: {response.status_code}")

        # Wait for 30 seconds before sending the next batch of data
        time.sleep(30)

# Run the function to start sending data
push_data_to_power_bi()
