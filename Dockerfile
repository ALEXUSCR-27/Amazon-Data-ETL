FROM apache/airflow:latest

COPY .env /opt/airflow/

USER root
RUN apt-get update && \
apt-get -y install git && \
apt-get clean


USER airflow
RUN pip install supabase python-dotenv
