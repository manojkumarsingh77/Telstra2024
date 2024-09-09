import random
import time
from datetime import datetime
import csv

# Define the output file (CSV format)
output_file = "real_time_telecom_data.csv"

# Define the columns for the dataset
columns = [
    "CustomerID", "Area", "CallID", "TotalCalls", "DroppedCalls", "DataUsageMB",
    "RoamingCharges", "Complaints", "PaymentDelay", "PlanID", "SatisfactionScore",
    "TransactionDate", "Region", "SMSID", "Response", "SubscriptionDate",
    "NetworkType", "SuccessfulCalls", "CallDuration", "RoamingCountry", "Revenue"
]

# Function to generate random telecom data
def generate_data():
    customer_id = random.randint(1, 1000)
    area = random.choice(["Area1", "Area2", "Area3", "Area4"])
    call_id = random.randint(1, 10000)
    total_calls = random.randint(50, 500)
    dropped_calls = random.randint(0, 50)
    data_usage_mb = random.uniform(0.5, 10.0)
    roaming_charges = random.uniform(0, 50)
    complaints = random.randint(0, 5)
    payment_delay = random.randint(0, 60)
    plan_id = random.randint(1, 5)
    satisfaction_score = random.uniform(1, 5)
    transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    region = random.choice(["North", "South", "East", "West"])
    sms_id = random.randint(1000, 9999)
    response = random.choice(["Yes", "No"])
    subscription_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    network_type = random.choice(["4G", "5G", "3G"])
    successful_calls = random.randint(10, 100)
    call_duration = random.uniform(1, 30)
    roaming_country = random.choice(["USA", "Canada", "UK", "Australia"])
    revenue = random.uniform(10, 200)
    
    return [
        customer_id, area, call_id, total_calls, dropped_calls, data_usage_mb,
        roaming_charges, complaints, payment_delay, plan_id, satisfaction_score,
        transaction_date, region, sms_id, response, subscription_date, network_type,
        successful_calls, call_duration, roaming_country, revenue
    ]

# Function to write data to CSV file
def write_to_csv(row):
    with open(output_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

# Main loop to generate and write data every 30 seconds
if __name__ == "__main__":
    # Write column headers once
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)

    # Infinite loop to generate data every 30 seconds
    while True:
        data_row = generate_data()
        write_to_csv(data_row)
        print(f"Data row written: {data_row}")
        time.sleep(30)  # Generates data every 30 seconds
