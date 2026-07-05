from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

# Adds the mapped scripts path to python runtime environment inside the docker container
# This allows Airflow to find and import your scripts/ingestion.py file

sys.path.insert(0, '/opt/airflow/scripts')
from ingestion import fetch_and_load

# Default settings applied to all tasks in this workflow loop
default_args = {
    'owner': 'data_engineering',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 2,                     # Retry 2 times if the Coingecko API rate-limits us
    'retry_delay': timedelta(minutes=3), # Wait 3 minutes before trying again
}

# Define the DAG, its schedule, and the tasks it will run
with DAG(
    dag_id='crypto_automation_etl',
    default_args=default_args,
    description='Hourly crypto ETL tracking via Airflow Standalone and MySQL Hooks',
    schedule_interval='0 * * * *',  # Cron expression: Runs precisely at minute 0 of every hour
    start_date=datetime(2026, 7, 1),
    catchup=False,  # Do not perform backfill for missed intervals
) as dag:
    
    # Task 1:Execute the full Python API extraction and database injection
    execute_pipeline = PythonOperator(
        task_id='fetch_and_store_crypto',
        python_callable=fetch_and_load
    )

    # Task 2: Define the task dependencies (if any)
    execute_pipeline