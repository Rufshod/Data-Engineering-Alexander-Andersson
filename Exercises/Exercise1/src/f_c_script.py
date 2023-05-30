import os
from datetime import datetime

# get the current directory of the current script:
script_dir = os.path.dirname(__file__)

# Event dates:
events = {
    "summer_break": datetime(2023, 6, 9, 15, 0),
    "lia_start": datetime(2023, 9, 25, 8, 0),
    "christmas": datetime(2023, 12, 24),
    "new_year": datetime(2024, 1, 1),
    "graduation_party": datetime(2024, 6, 9, 16, 30)
}

# Define logs directory path:
logs_dir = os.path.join(script_dir, "..", "logs")

# Create logs directory if it does not exist:
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Define path of the log file:
log_file = os.path.join(logs_dir, "countdown.log")


# create or open file inside logs directory:
with open(log_file, "w") as f:

    #Write current date and time:
    f.write(f"-------------------------------------------------\nCountdown from {datetime.now()}\n-------------------------------------------------\n\n")
    # Write each event and the remaining time until it:
    for event, event_date in events.items():
        time_left = event_date - datetime.now()
        f.write(f"Countdown to {event}: {time_left.days} days, {time_left.seconds // 3600} hours, {(time_left.seconds // 60) % 60} minutes\n")
        #print(f"Countdown to {event}: {time_left.days} days, {time_left.seconds // 3600} hours, {(time_left.seconds // 60) % 60} minutes\n")