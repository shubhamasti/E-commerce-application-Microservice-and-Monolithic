# Use the official Python image as base
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Initialize the MySQL database
RUN mysql -h host.docker.internal -u root -proot1234 < database.sql

# Run insert script to populate products
RUN python insert_script.py

# Expose the port on which your Flask app runs
EXPOSE 8082

# Command to run the Flask application
CMD ["python", "app.py"]