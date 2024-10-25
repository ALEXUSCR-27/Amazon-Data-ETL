from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from plugins.extract_plugin import extract_pl

dag = DAG(
    'ETL_pipeline',
    default_args={'start_date':days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_pl,
    dag=dag
)

extract_task