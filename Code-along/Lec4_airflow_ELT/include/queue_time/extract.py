
#%%
from airflow.operators.python import PythonOperator
import requests, pytz #pytz is used for timezone handling
from airflow.decorators import task_group
from datetime import datetime

theme_park = {"liseberg": 11, "asterix": 9}


stockholm_timezone = pytz.timezone("Europe/Stockholm") #TODO: check how timezones work in python

#%%

def _extract_queue_time():
    response = requests.get(f"https://queue-times.com/parks/{theme_park}/queue_times.json")

    if response.status_code == 200:
        return response.json()["rides"]


@task_group(group_id="extract_liseberg")
def extract_queue_time():
    extract_queue_time = PythonOperator(
        task_id="extract_queue_time",
        python_callable=_extract_queue_time
    )