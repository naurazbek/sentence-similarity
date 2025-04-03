# Use an official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose a port (if needed for a web app, e.g., Flask)
# EXPOSE 5000

# Run the application
CMD ["python", "main.py"]