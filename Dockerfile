# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY app.py .

# Use the -u flag to force standard streams (stdout/stderr) to be unbuffered.
# This ensures logs stream immediately to Harness UI.
CMD ["python", "-u", "app.py"]
