from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaTelecomDataStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1") \
    .getOrCreate()

# Read streaming data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test1") \
    .load()

# Cast key and value from Kafka topic to strings and print them to the console
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Output the raw data from Kafka to the console
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()




spark-submit --master local[2] \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.3 \
streamingkafka1.py

