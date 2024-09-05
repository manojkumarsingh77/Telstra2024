# Install PySpark in Colab
!pip install pyspark

# Import PySpark modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("TelecomCallDataAnalysis").getOrCreate()

# Sample call data for telecommunications (similar to the flight data example)
data = [
    ("United States", "India", 15),   # 15-minute call from US to India
    ("United States", "Canada", 10),  # 10-minute call from US to Canada
    ("India", "United States", 25),   # 25-minute call from India to US
    ("Canada", "United States", 20),  # 20-minute call from Canada to US
    ("United States", "India", 35),   # 35-minute call from US to India
    ("United States", "Canada", 5),   # 5-minute call from US to Canada
    ("India", "Canada", 30),          # 30-minute call from India to Canada
    ("Canada", "India", 40)           # 40-minute call from Canada to India
]

# Define schema for the DataFrame
columns = ["DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME", "call_duration"]

# Create a DataFrame
call_data = spark.createDataFrame(data, schema=columns)

# Show the original call data
print("Original Call Data:")
call_data.show()

# Step 1: Repartition the data (Transformation)
call_data_repartition = call_data.repartition(3)

# Step 2: Filter the calls where the destination is the United States (Transformation)
us_calls_data = call_data.filter(col("DEST_COUNTRY_NAME") == "United States")

# Step 3: Further filter calls where the origin is either India or Canada (Transformation)
us_india_canada_calls = us_calls_data.filter(
    (col("ORIGIN_COUNTRY_NAME") == "India") | 
    (col("ORIGIN_COUNTRY_NAME") == "Canada")
)

# Step 4: Group by destination country and sum the call duration (Transformation)
total_call_duration_by_dest = us_india_canada_calls.groupby("DEST_COUNTRY_NAME").sum("call_duration")

# Step 5: Show the result (Action)
print("Total Call Duration for Calls to the United States from India or Canada:")
total_call_duration_by_dest.show()
