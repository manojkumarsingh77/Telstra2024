from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, FloatType, DoubleType

# Initialize Spark session with Kafka support
spark = SparkSession.builder \
    .appName("KafkaTelecomDataStreaming") \
    .getOrCreate()

# Define the schema for the incoming telecom data
schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("call_duration", IntegerType()) \
    .add("data_usage", FloatType()) \
    .add("location", StringType()) \
    .add("call_type", StringType()) \
    .add("timestamp", DoubleType())

# Read the streaming data from the Kafka topic 'telecom-data'
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "telecom-data") \
    .load()

# Convert the value column from binary to string and parse the JSON data
df = df.selectExpr("CAST(value AS STRING) as json_value")
json_df = df.select(from_json(col("json_value"), schema).alias("data")).select("data.*")

# Process the streaming data (e.g., filter calls longer than 100 seconds)
filtered_df = json_df.filter(col("call_duration") > 100)

# Write the filtered data to the console in real time
query = filtered_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the termination signal
query.awaitTermination()
