# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables (customize as needed)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the working directory
COPY main_api.py /app/

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Define the command to run your Python application
CMD [ "python", "main_api.py" ]
