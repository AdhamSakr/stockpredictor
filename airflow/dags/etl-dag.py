from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime


dag = DAG(
    "etl_dag",
    default_args={"start_date": datetime.today()},
    schedule_interval="0 3 * * *",
    catchup=False,
)

etl_task = DockerOperator(
    task_id="run_docker_image",
    image="adhamsakr/stockpredictor-etl:latest",
    api_version="1.37",
    docker_url="TCP://docker-socket-proxy:2375",
    network_mode="bridge",
    auto_remove=True,
    dag=dag,
)

etl_task
