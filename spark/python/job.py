#!/venv/bin
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import functions as fspk
from pyspark.sql.types import StringType, IntegerType, DateType, TimestampType
import os 
import pandas as pd 

#base path
# /Users/jcvpalma/Projetos/JobTests/jcvpalma_test_repository/spark/python
base_path = os.path.dirname(os.path.abspath(__file__))

#app name
app_name  = "TestJob"

if __name__ == "__main__":
    #instance of spark session
    spk = SparkSession.builder \
        .master("local") \
        .appName(app_name) \
        .getOrCreate()

    #define the file path
    data_file = "{}/data/input/users/load.csv".format(base_path)
    #output files
    outdata_file = "{}/data/output/task1/load_1".format(base_path)
    outdata_file2 = "{}/data/output/task1/load_2".format(base_path)

    
    #load to dataframe
    spk_df = spk.read.csv(data_file, header=True, sep=",").cache()
    #ok, check if I read correct
    if spk_df.count() > 0:
        print("File read! Total rows: {} ".format(spk_df.count()))

        #show the content file
        spk_df.show()

        #first action is convert this file to another format and justify the option
        #convert tsv
        #spk_df.write.format('com.databricks.spark.csv').save(outdata_file, header=True, sep="\t")
        print("1. Save file in format CSV tabular!")
        print("""   convert into CSV with tabular because : 
                        1. CSV it's most common format file and can be imported in many others projects and tools
                        2. separate the columns in a tab mode means that its readable for human better than if I separated by comma or semicolon as well.""")

        # get the columns
        v_columns = spk_df.schema.names

        print("2. group by the data and get the last rows!")
        #read the file of last task
        df_task1 = spk.read.csv("{}/part-00000-12162fd3-9c28-4f41-8c92-308de011cff5-c000.csv".format(outdata_file), header=True, sep="\t")
        
        #group by the id and using agg max I can create a new df to join in inner with the first df
        df_distinct = df_task1.select(["id", "update_date"]) \
            .groupby(["id"]) \
            .agg(fspk.max("update_date").alias('update_date'))
        print("result of distinct data")
        df_distinct.show()

        print("get the uniques rows by max update_date")
        df_task2 = spk.createDataFrame(df_task1.join(df_distinct, ["id", "update_date"], 'inner')\
            .select(v_columns).collect(), schema=v_columns) \
                .withColumn("age", fspk.col("age").cast(IntegerType())) \
                .withColumn("update_date", fspk.col("update_date").cast(TimestampType())) \
                .withColumn("update_date", fspk.col("create_date").cast(TimestampType()))

        print("result of join dfs")
        df_task2.printSchema()
        df_task2.show()
        
        print("save file task2 and 3 in the same time!")
        #df_task2.write.format('com.databricks.spark.csv').save(outdata_file2, header=True, sep="\t")

        print("finish the test!")

    else:
        print("No read the file!")

    