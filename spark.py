from pyspark.sql import SparkSession


# 1. Initialize a Spark Session
# "local[*]" tells Spark to use all available CPU cores on your machine
import os
from pyspark.sql import SparkSession
# 1. Force the driver to bind to your specific LAN desktop name 
# Replace 'desktop.lan' with your actual machine's local network hostname

# Build the local session
spark = SparkSession.builder \
    .appName("Test") \
    .master("local[*]") \
    .getOrCreate()

# Verify the connection works
df  = spark.read.format("csv").option("header","true").load("CPI_Out.csv")
df.show()
# Always stop the session at the end
spark.stop()

# UI is now live at http://localhost:4040
#df_2 = spark.read.csv('CPI_Out.csv')
#print(df_2.head())
# 2. Create sample data
#data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
#columns = ["Name", "Age"]

# 3. Create a DataFrame
#df = spark.createDataFrame(data, schema=columns)

# 4. Show the data
#print("Original DataFrame:")
#df_2.show()

# 5. Perform a basic transformation (Filter and Select)
#print("Filtered Data (Age > 30):")
#df.filter(df.Age > 30).select("Name").show()

# 6. Stop the session
#spark.stop()