# END-TO-END DATA ENGINEERING SYSTEM (kafka,spark,airflow,postgres,docker)

## Overview
Let’s break down the data pipeline process step-by-step:

1. **Data Streaming**: Initially, data is streamed from the API into a Kafka topic.
2. **Data Processing**: A Spark job then takes over, consuming the data from the Kafka topic and transferring it to a PostgreSQL database.
3. **Scheduling with Airflow**: Both the streaming task and the Spark job are orchestrated using Airflow. While in a real-world scenario, the Kafka producer would constantly listen to the API, for demonstration purposes, we’ll schedule the Kafka streaming task to run daily. Once the streaming is complete, the Spark job processes the data, making it ready for use.

- All of these tools will be built and run using docker, and more specifically docker-compose.