FROM apache/airflow:latest

COPY dags/ /opt/airflow/dags/
COPY data/ /opt/airflow/data/

USER root
RUN apt-get update && \
apt-get -y install git && \
apt-get clean

USER airflow
