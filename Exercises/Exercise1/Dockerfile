FROM python:3.9

# Add the entire src directory to the container at /Exercise1/src
ADD src /Exercise1/src

# Installing required packages with pip
RUN pip install matplotlib plotly_express pandas numpy dash sklearn


# Specify the working directory as /Exercise1 inside the container
WORKDIR /Exercise1

#Apply the cron job



# Run ex1_0_setup.py when the container starts
CMD ["python", "src/ex1_0_setup.py"]
