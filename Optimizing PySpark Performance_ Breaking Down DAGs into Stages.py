# Databricks notebook source
from pyspark.sql import SparkSession 
import os



data = [("Alice", 25),("Bob", 30),("Charlie", 35),("David", 28),("Eva", 40),("Frank", 32),("Grace", 29)]
columns = ["Name","Age"]
df = spark.createDataFrame(data,columns)



num_cores = os.cpu_count()
print(f"number of cores: {num_cores}")



core_pct = 0.8 
df = df.repartition(int(core_pct * num_cores))



df1 = df 
df2 = df1.filter(df1['Age'] > 30)



result1 = df1.collect()
result2 = df2.collect()




