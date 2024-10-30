FROM apache/airflow:latest

COPY .env /opt/airflow/

# COPY dags/ /opt/airflow/dags/
# COPY data/ /opt/airflow/data/
# COPY plugins/ /opt/airflow/plugins
# COPY utils/ /opt/airflow/utils

USER root
RUN apt-get update && \
apt-get -y install git && \
apt-get clean


USER airflow
RUN pip install supabase python-dotenv
