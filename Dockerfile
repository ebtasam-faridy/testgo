# Use a lean base image for your application
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the image
COPY app.py .

# Command to run the application
# This is the command whose STDOUT/STDERR is captured by Harness
CMD ["python", "app.py"]
