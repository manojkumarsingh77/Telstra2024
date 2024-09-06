#Project 1: Customer Data Usage and Billing Analytics (Telecommunications)
#Data Generation Script:

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate synthetic data for customer data usage and billing
def generate_customer_data(num_records=1000):
    # Sample data for regions and plans
    regions = ['North', 'South', 'East', 'West', 'Central']
    plans = ['Basic', 'Standard', 'Premium']
    
    # Generate current date
    current_time = datetime.now()
    
    # Generate synthetic data
    data = {
        'CustomerID': [f'CID{str(i).zfill(4)}' for i in range(1, num_records+1)],
        'Region': [random.choice(regions) for _ in range(num_records)],
        'Plan': [random.choice(plans) for _ in range(num_records)],
        'DataUsageGB': np.random.normal(15, 5, num_records).round(2),  # Data usage between 10-20 GB
        'BillingAmount': np.random.normal(50, 20, num_records).round(2),  # Billing amount with some variance
        'Overcharges': np.random.normal(5, 3, num_records).round(2),  # Additional charges for exceeding data
        'Date': [current_time.strftime("%Y-%m-%d")] * num_records,
    }
    
    df = pd.DataFrame(data)
    
    # Save as CSV
    df.to_csv('/content/customer_data_usage.csv', index=False)
    print(f"Customer data generated at {current_time}")
    
# Schedule this to run as a cron job every 30 minutes
generate_customer_data()
import time

# Run the script every 30 minutes
while True:
    generate_customer_data()
    # Wait for 1800 seconds (30 minutes) before running again
    time.sleep(1800)

#Steps to Run as a Cron Job in Google Colab:

#Use the time library to add delays and loops for running the data generation script every 30 minutes.
#The generated file customer_data_usage.csv will be updated at each interval.



#Project 2: Network Performance Monitoring and Outage Detection (Telecommunications)
#Data Generation Script:

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate synthetic data for network performance
def generate_network_performance_data(num_records=1000):
    # Sample data for regions and time intervals
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    # Generate current time
    current_time = datetime.now()
    
    # Generate synthetic data
    data = {
        'Region': [random.choice(regions) for _ in range(num_records)],
        'SignalStrength': np.random.uniform(1, 5, num_records).round(2),  # Signal strength between 1 to 5 bars
        'CallDropRate': np.random.uniform(0, 5, num_records).round(2),  # Call drop rate as percentage
        'DataTransferSpeed': np.random.uniform(10, 100, num_records).round(2),  # Data speed in Mbps
        'OutageDetected': [random.choice([0, 1]) for _ in range(num_records)],  # 0: No Outage, 1: Outage detected
        'DateTime': [current_time.strftime("%Y-%m-%d %H:%M:%S")] * num_records,
    }
    
    df = pd.DataFrame(data)
    
    # Save as CSV
    df.to_csv('/content/network_performance_data.csv', index=False)
    print(f"Network performance data generated at {current_time}")
    
# Schedule this to run as a cron job every 15 minutes
generate_network_performance_data()

#Steps to Run as a Cron Job in Google Colab:

#Use the time library to add delays and loops for running the data generation script every 15 minutes.
#The generated file network_performance_data.csv will be updated at each interval.

import time

# Run the script every 15 minutes
while True:
    generate_network_performance_data()
    # Wait for 900 seconds (15 minutes) before running again
    time.sleep(900)


