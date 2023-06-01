# Import necessary libraries
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from twitter_etl import run_twittter_etl  # Import the ETL function from the twitter_etl script

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',  # Owner of the DAG
    'depends_on_past': False,  # The DAG does not have dependencies on past runs
    'start_date': datetime(2023, 5, 30),  # The date/time this DAG will start
    'email': ['airflow@example.com'],  # Email to notify in case of issues
    'email_on_failure': False,  # No email will be sent on failure
    'email_on_retry': False,  # No email will be sent on retry
    'retries': 1,  # Number of retries if the DAG fails
    'retry_delay': timedelta(minutes=1)  # Delay between retries
}

# Define the DAG
dag = DAG(
    'twitter_dag',  # The DAG's ID
    default_args=default_args,  # The default arguments
    description='Experimental ETL code'  # Description of the DAG
)

# Define the task that will run the ETL function
run_etl = PythonOperator(
    task_id='complete_twitter_etl',  # The task's ID
    python_callable=run_twittter_etl,  # The function to run
    dag=dag  # The DAG that this task belongs to
)

run_etl  # This is required to let Airflow know this task is part of the DAG
