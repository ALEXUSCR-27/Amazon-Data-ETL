from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from plugins.extract_tasks import extract_f

dag = DAG(
    'extract_dag',
    default_args={'start_date':days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)

print_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_f,
    dag=dag
)

print_task