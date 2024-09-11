import random
import datetime
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

# Create a Spark session
spark = SparkSession.builder.appName("TelecomDataGenerator").getOrCreate()

# Utility function to save DataFrame to DBFS
def save_to_dbfs(df: DataFrame, path: str):
    df.write.mode("overwrite").parquet(path)
    print(f"Data saved to {path}")

# Exercise 1: Customer Call Data
def generate_call_data():
    data = [(random.randint(1000, 1010), round(random.uniform(1.0, 60.0), 2), 
             datetime.date(2023, random.randint(1, 12), random.randint(1, 28))) for _ in range(100)]
    df = spark.createDataFrame(data, ["customer_id", "call_duration", "call_date"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/call_data")

# Exercise 2: Dropped Call Detection
def generate_dropped_call_data():
    data = [(random.randint(1000, 1010), bool(random.getrandbits(1)), 
             round(random.uniform(0.5, 60.0), 2)) for _ in range(200)]
    df = spark.createDataFrame(data, ["customer_id", "call_dropped", "call_duration"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/dropped_call_data")

# Exercise 3: Average Call Duration by Month
def generate_monthly_call_data():
    data = [(random.randint(1000, 1010), round(random.uniform(1.0, 60.0), 2), 
             datetime.date(2023, random.randint(1, 12), random.randint(1, 28))) for _ in range(200)]
    df = spark.createDataFrame(data, ["customer_id", "call_duration", "call_date"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/monthly_call_data")

# Exercise 4: Billing Discrepancy Detection
def generate_billing_data():
    data = [(random.randint(1000, 1010), round(random.uniform(10.0, 100.0), 2), 
             round(random.uniform(0, 20.0), 2)) for _ in range(100)]
    df = spark.createDataFrame(data, ["customer_id", "actual_charge", "extra_charge"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/billing_data")

# Exercise 5: SMS Campaign Effectiveness
def generate_sms_campaign_data():
    data = [(random.randint(1, 5), bool(random.getrandbits(1))) for _ in range(200)]
    df = spark.createDataFrame(data, ["campaign_id", "response"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/sms_campaign_data")

# Exercise 6: Network Outage Impact Analysis
def generate_outage_data():
    data = [(random.randint(1000, 1010), bool(random.getrandbits(1)), 
             round(random.uniform(1.0, 60.0), 2)) for _ in range(100)]
    df = spark.createDataFrame(data, ["customer_id", "network_outage", "call_duration"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/outage_data")

# Exercise 7: Customer Satisfaction Analysis
def generate_satisfaction_data():
    data = [(random.randint(1000, 1010), random.randint(1, 5)) for _ in range(200)]
    df = spark.createDataFrame(data, ["customer_id", "satisfaction_score"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/satisfaction_data")

# Exercise 8: Fraud Detection in SIM Usage
def generate_sim_usage_data():
    data = [(random.randint(1000, 1010), round(random.uniform(100, 5000), 2)) for _ in range(100)]
    df = spark.createDataFrame(data, ["customer_id", "sim_usage"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/sim_usage_data")

# Exercise 9: Roaming Usage Analysis
def generate_roaming_usage_data():
    data = [(random.randint(1000, 1010), round(random.uniform(10.0, 100.0), 2)) for _ in range(100)]
    df = spark.createDataFrame(data, ["customer_id", "roaming_charge"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/roaming_data")

# Exercise 10: Customer Churn Prediction
def generate_customer_churn_data():
    data = [(random.randint(1000, 1010), round(random.uniform(1.0, 60.0), 2), 
             bool(random.getrandbits(1)), random.randint(1, 5), bool(random.getrandbits(1))) for _ in range(200)]
    df = spark.createDataFrame(data, ["customer_id", "call_duration", "call_dropped", 
                                      "satisfaction_score", "churn"])
    save_to_dbfs(df, "/dbfs/tmp/telecom/churn_data")

# Execute the data generation functions for each exercise
generate_call_data()
generate_dropped_call_data()
generate_monthly_call_data()
generate_billing_data()
generate_sms_campaign_data()
generate_outage_data()
generate_satisfaction_data()
generate_sim_usage_data()
generate_roaming_usage_data()
generate_customer_churn_data()
