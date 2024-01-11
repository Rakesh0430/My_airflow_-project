from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ml_workflow',
    default_args=default_args,
    description='End-to-End ML Workflow with Airflow',
    schedule_interval=timedelta(days=1),
)

def preprocess_data():
    os.system("python scripts/data_processing.py")

def train_model():
    os.system("python scripts/model_training.py")

preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

preprocess_task >> train_task
