import subprocess
import sys

print("Running sript.py Python script")

# running the installed_packages.sh script in the Exercise1 folder
subprocess.call(['sh', '../installed_packages.sh'])

# Printing python version
print("Python version")
print(sys.version)