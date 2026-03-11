# Databricks notebook source
# Q1 What are the fundamental differences between RDDs, Dataframes, and Datasets in Spark?  

basic fundamental main differences : 
    
RDD are not structured , they are not optimized , you cannot run any sql queries over them , typechecking at the compile time
use: complex transformation and unstructured data

DataFrame are build on RDD but they are strucuted they follow schema and they are optimized they use the catalyst optimizer and tungsten engine for better execution 
they are typed check at the run time 
use : sql queries and analysis 

Datasets are build on DataFrames but they have the type checking while compile time 
use : typed check sql query

# COMMAND ----------

# Q2 Explain the execution plan of a Spark query and describe the role and functioning of the Catalyst Optimizer in Apache Spark’s execution process. 

spark query execution plan :
 
User writes query (SQL / DataFrame API)
Logical Plan created
Catalyst Optimizer transforms logical plan
Physical Plan generated
DAG Scheduler creates stages
Tasks executed on executors

Function of Catalyst Optimizer
IT is core query optimization framework in Apache Spark SQL that automatically transforms SQL and DataFrame queries into highly efficient execution plans

To create the optimized logical plan for the 

Unresolved Logical Plan : It is the first plan created in this the optimizer create a rough plan of what is happening in the query , it doesnt not validate 

Analysis Logical Plan : Spark analyzes the logical plan to resolve references to table columns, data types, and function names using the catalyst analyzer.

Logical Optimization Plan: This stage applies standard rules to improve efficiency, such as 
constant folding, 
column pruning and predicate pushdown

Physical Logical Plan : Catalyst generates multiple physical plans for the logical plan and uses cost-based optimization to choose the most efficient one based on table statistics 

Code Generation : Finally, the optimizer generates JVM bytecode to run the query efficiently on each machine, often using Scala quasiquotes to generate code at runtime.


# COMMAND ----------

# Q3 Create a DataFrame containing customer details and save it in a TXT format with the file name "customer.txt". 
from pyspark.sql.types import *

data = ([1, 'arun' , 12],
        [2,'pratap',13],
        [3,'singh',14])
schema = StructType([
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('age', IntegerType(), True)
]
)

df = spark.createDataFrame(data , schema = schema)
df.show()

df.write.parquet("dbfs:/FileStore/Week6_Spark/object")

# COMMAND ----------

# Define a Quartz cron expression to schedule a job to run at 3 AM every Monday and Wednesday, during January and March, in the UTC time zone and Cron expression to schedule a job to run every 30 minutes from 8 AM to 5 PM, on weekdays (Monday to Friday), in the UTC time zone. 

0 0 3 ? 1,3 Mon,Wed *  
0/30 8-17 ? * Mon-Fir *

# COMMAND ----------

# Provide a comprehensive explanation of cluster configurations, autoscaling benefits, and resource allocation strategies in Databricks. Elaborate on Delta Lake as a technology. Explain its advantages and key features compared to other file formats like Parquet, Avro, ORC, CSV, Text, and JSON.Cluster configuration refers to the process of connecting multiple independent computers—known as nodes—into a single, unified system that works together to enhance performance, availability, and scalability

Components of cluster : 
    Cluster contains the group of nodes , which are connected over a network and share resources in the case of map reduce and data transmissions

Each cluster contains the 
1. Driver node : the one who check the status of the execution and maintains the failure and schedule the jobs

2. Worker node : the one who executes the job assign by the driver 

3. Executors : the worker node contains the multiple executors and they  taks do the acutal implementation of the task they run parallely like they execute the taks together

Types of cluster mode 
Client mode : where the driver runs on the client machine and the executors are on the clusters.
Cluster mode : here the driver and executors both are on the cluster of nodes.
Local mode : here both the driver and the executors are at the same node 

Type of Clusters : 
    Serverless clusters:
        Serverless clusters are fully managed,that automatically scale capacity based on demand, eliminating the need for manual provisioning or server management. 
    All pupose Clusters:
       All-purpose clusters are interactive, user-managed compute resources designed for integrated code development, and collaboration. They allow multiple users to run queries and notebooks, supporting flexible, manual scaling and termination
    Job Clusters:
        Databricks job clusters are cost-effective compute resources that automatically spin up to execute specific, scheduled, or automated tasks (like ETL pipelines) and terminate immediately upon completion
    Sql Warehouse Cluster:
        SQL warehouses are specialized, compute-optimized clusters designed for running SQL queries, BI reporting, and analytics, rather than general-purpose workloads.
    

Autoscaling improves application performance and reliability by automatically adjusting compute resources to meet real-time demand, preventing downtime during traffic spikes

Delta Lake is an open-source storage layer that enhances data lakes by providing a transactional data management framework, effectively combining the flexibility of a data lake with the reliability of a data warehouse.

ACID Transactions
Time Travel (Data Versioning)
Schema Enforcement and Evolution
Unified Batch and Streaming
Efficient DML Operations
Performance Optimization

# COMMAND ----------

#Using Databricks Notebooks, demonstrate the practical utility of magic commands by performing the following tasks: 

# Create a new cell with %sql magic and execute a SQL query to retrieve and display data from an existing table within the notebook. 

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Arun", 25),
    (2, "Pratap", 28),
    (3, "Singh", 30)
]

columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
df.write.mode("overwrite").saveAsTable("table1")

%sql 
select * from table1 
#not able to store the table1 into the databricks due to the limitations 

# COMMAND ----------

# MAGIC %fs head dbfs:/Workspace/Repos/arunofficial1729@gmail.com/
# MAGIC
# MAGIC %fs ls dbfs:/Workspace/Repos/arunofficial1729@gmail.com/
# MAGIC
# MAGIC # %fs cp file:/Workspace/Users/arunofficial1729@gmail.com/LoadingData/
# MAGIC
# MAGIC dbfs:/Workspace/Repos/arunofficial1729@gmail.com/
# MAGIC
# MAGIC

# COMMAND ----------

# Utilize %run magic to execute another notebook or file within the current notebook and display the output. Also send a variable from the caller notebook and print the value in another notebook. 
name = "Arun Pratap Singh"

# COMMAND ----------

output = %run ./helper_notebook $username=name

print("Returned value from child notebook:")
print(output)

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC # In a Markdown cell (%md), create formatted text to explain the process and results obtained from the executed SQL query or file operations. 
# MAGIC ###Hedading###
# MAGIC

# COMMAND ----------

# You have a dataset requiring substantial computation (20-30GB). Design a Databricks cluster with optimal configurations for processing this data efficiently. Explain your choice of instance types, node count, and autoscaling parameters based on the workload characteristics.  


# ans : Having Doubt about like what to do in this question

# COMMAND ----------

import math

dbutils.widgets.removeAll()
dbutils.widgets.text("Input", "")

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True


number = dbutils.widgets.get("Input")

numbers = [int(x.strip()) for x in number.split(",") if x.strip() != ""]

for n in numbers:
    if is_prime(n):
        print(f"{n} is a Prime Number")
    else:
        print(f"{n} is NOT a Prime Number")

# COMMAND ----------

# grouped_df.show()
# repartitioned_df.show()
# ranked_df.show()

total_job = 3

# grouped_df = transactions_df.groupBy('category') \
#     .agg(sum('amount').alias('total_amount')

stage1= groupBy() -> 200 tasks
stage2= agg() -> 200 tasks in general 

# repartitioned_df = transactions_df.repartition(5)
stage1= ReadData -> 200 tasks 
stage2 = repartition() -> 5 tasks

#Window.partitionBy('category').orderBy(col('timestamp').desc()) 
stage1 = partitionBy() task -> 200
stage2 = orderBy() task -> 200

# ranked_df = transactions_df.withColumn('transaction_rank', rank().over(window_spec)) 
stage1 = rank() 
tasks = 200

Total Jobs → 3

Total Stages → 7

Tasks:

Job 1 → 400 tasks

Job 2 → 205 tasks

Job 3 → 600 tasks

Total Tasks = 1205 




