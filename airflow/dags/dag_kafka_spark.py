from airflow import Dag
from datetime import timedelta,datetime
from airflow.operators.python import PythonOperator
from airflow.providers.ocker.operators.docker import 

start_date = datetime.today() - timedelta(days=1)

default_args = {
    "owner":"airflow",
    "start_date": start_date,
    "retries": 1,
    "retries_delay": timedelta(seconds=5)
}

with Dag(
    dag_id ="kafka_spark_dag",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catch_up=False
) as dag:
    
    kafka_stream_task = PythonOperator(
        task_id="kafka_data_stream",
        python_callable=,
        dag = dag
    )

    spark_stream_task = DockerOperator()