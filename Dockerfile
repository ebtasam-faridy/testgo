# Use the pushed "broken" arm64 image (actually amd64)
FROM ebtasamfaridy/python:3.9-slim-linux-arm64

WORKDIR /app

COPY app.py .

# This RUN will trigger QEMU / ELF failure on arm64 hosts
RUN echo "Testing broken base image"

# Use the -u flag to force stdout/stderr unbuffered
CMD ["python", "-u", "app.py"]
