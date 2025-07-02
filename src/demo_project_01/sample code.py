from pyspark.sql.functions import col, lit

table = "samples.nyctaxi.trips"

df = spark.read.table(table)

df.select("fare_amount", "trip_distance", "pickup_zip").limit(10).show()