from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringField
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(funcName)s:%(levelname)s:%(message)s")

def create_spark_session()->SparkSession:
    spark = (SparkSession.bulder.appName("Postgress sinking").config("spark.jars.packages",
                                                                     "org.postgresql:postgresql:42.54,org.apache.spark:spark-sql-kafka-0-10-12.12:3.5.0").getOrCreate())
    logging.info("Successfully created sparksession ....")
    return spark

def create_initial_df(SparkSession):
    pass
def create_final_df(df):
    pass
def start_stream(df_parsed,spark):
    pass
def write_to_postgres():
    pass

if __name__ == "__main":
    write_to_postgres()

