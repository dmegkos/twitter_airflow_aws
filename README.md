# Twitter ETL Pipeline with Apache Airflow and AWS

This project demonstrates an ETL (Extract, Transform, Load) pipeline which retrieves recent tweets, processes them into a tabular format, and stores the output in a CSV file on AWS S3. The entire pipeline is automated using Apache Airflow and the computations are performed on an AWS EC2 instance.

## Project Structure

The project consists of two main Python scripts:

1. `twitter_etl.py`: This script contains the function `run_twitter_etl()`, which extracts tweets using the Twitter API and Tweepy, transforms the data into a DataFrame using Pandas, and loads the DataFrame as a CSV file to an S3 bucket.

2. `twitter_dag.py`: This script defines an Apache Airflow DAG (Directed Acyclic Graph), which orchestrates the execution of the ETL pipeline on a schedule.

## Requirements

- A Twitter Developer Account with an assigned Bearer Token.
- An AWS account with an S3 bucket available for storing data.
- An AWS EC2 instance with Apache Airflow and all required Python libraries installed.
- The EC2 instance should accept inbound connections IPv4 to port 8080 to allow access to the Apache Airflow admin portal.
- Ensure you have the appropriate IAM rules enabled so that the EC2 instance can write to the S3 bucket.

## Usage

To run the ETL process, use the Airflow CLI to trigger the DAG defined in `twitter_dag.py`.

```bash
airflow dags trigger twitter_dag
```

Please replace the placeholder email and start_date in twitter_dag.py with your own details.