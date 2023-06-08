from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime
from pathlib import Path

date_lake_path = Path(__file__).parents[1] / "data" / "datalake"

data_warehouse_path = Path(__file__).parents[1] / "data" / "datawarehouse"

time_variable = "$(date +%y%m%d_%H%M%S)"

joke_api = "https://official-joke-api.appspot.com/random_joke"

with DAG(dag_id = "joke_DAG", start_date = datetime(2023,6,1)):
    say_hello = BashOperator(
        task_id = "say_hello",
        bash_command = "echo 'hello, it is time for a joke: '",)
    
    setup_folders = BashOperator(
        task_id = "setup_folders",
        bash_command = f"mkdir -p {date_lake_path} {data_warehouse_path}")

    download_joke = BashOperator(
        task_id = "random_joke",
        bash_command = f"curl -o {date_lake_path}/joke_{time_variable}.json {joke_api}" )
    
    say_hello >> setup_folders >> download_joke
