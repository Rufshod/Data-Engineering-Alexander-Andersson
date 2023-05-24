import subprocess
print("run")

#changing directory to the Exercise1 folder
subprocess.call(['cd', '../'])
# running the installed_packages.sh script in the Exercise1 folder
subprocess.call(['./installed_packages.sh'])