from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType
from pyspark.sql.functions import col,from_json
import logging
from src.constants import DB_FIELDS,POSTGRES_URL,POSTGRES_PROPERTIES

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(funcName)s:%(levelname)s:%(message)s")

def create_spark_session()->SparkSession:
    spark = (SparkSession.bulder.appName("Postgress sinking").config("spark.jars.packages",
                                                                     "org.postgresql:postgresql:42.54,org.apache.spark:spark-sql-kafka-0-10-12.12:3.5.0").getOrCreate())
    logging.info("Successfully created sparksession ....")
    return spark

def create_initial_df(SparkSession):
    try:
        df = (SparkSession.readStream.format("kafka")
        .option("kafka.bootstrap.servers","kafka:9092")
        .option("subscribe","rappel_conso")
        .option("startingOffset","earlist")
        .load())
        logging.info("Initial Dataframe created successfully")
    except Exception as e:
        logging.warning(f"Initial dataframe couldn't be created due to exception {e}")
def create_final_df(df):
    schema = StructType(StructField[field_name,StringType(),True]
    for field_name in DB_FIELDS)
    df_out = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"),schema).alias("data")).select("data.*")
    return df_out
def start_stream(df_parsed,spark):
    existing_data_df=spark.read.jdbc(POSTGRES_URL,"rappel_conso",properties=POSTGRES_PROPERTIES)
    unique_column = "refernce_fiche"
    logging.info("Start streaming.......")
    query = df_parsed.writeStream.forEachBatch(lambda batched_df,_:(
        batched_df.join(existing_data_df[unique_column]==existing_data_df[unique_column],"leftanti").write.jdbc(
            POSTGRES_URL,"rappel_conso","append",properties=POSTGRES_PROPERTIES
        )
    )).trigger(once=True).start()
    return query.awaitTermination()
def write_to_postgres():
    spark=create_spark_session()
    df = create_initial_df()
    df_final = create_final_df()
    start_stream(df_final,spark=spark)

if __name__ == "__main":
    write_to_postgres()

