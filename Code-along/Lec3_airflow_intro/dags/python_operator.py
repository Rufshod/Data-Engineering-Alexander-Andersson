from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from pathlib import Path
import numpy as np


simulation_path = Path(__file__).parents[1]/"data"/"dice_simulatons"

def _dice_rolls(number_rolls):
    return list(np.random.randint(1,7, size = number_rolls))

def _save_dice_rolls(task_instance):
    simulation_data = task_instance.xcom_pull(
        task_ids = ["dice_rolls"])
        #validation code
        
    with open(simulation_path/"dice_rolls.txt", "a") as file:
        file.write(f"Dice rolls {datetime.now()}\n")
        file.write(f"{simulation_data}\n\n")


with DAG(dag_id = "dice_simulator", start_date = datetime(2023,6,7), 
         schedule = "*/30 8 * * *", # every 30 minutes at 8am every day 
         # 08:30, 09:00 ... 23:30
         catchup=True): 
    setup_directories = BashOperator(
        task_id = "setup_directories",
        bash_command = f"mkdir -p {simulation_path}"
    )
    dice_rolls = PythonOperator(
        task_id = "dice_rolls",
        python_callable = _dice_rolls,
        op_kwargs = { "number_rolls": 10},
        do_xcom_push = True
    )
    save_dice_rolls = PythonOperator(
        task_id = "save_dice_rolls",
        python_callable = _save_dice_rolls
    )


    setup_directories >> dice_rolls >> save_dice_rolls