from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from scripts.extract_plugin import extract_data
from scripts.transform_plugin import transform_data
from scripts.load_plugin import load_data_db


dag = DAG(
    'ETL_pipeline',
    default_args={'start_date':days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load_data_db,
    dag=dag
)

extract_task>>transform_task>>load_task