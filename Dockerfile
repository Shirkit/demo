# Use an NVIDIA base image so the GPU is accessible
FROM nvidia/cuda:12.1.0-base-ubuntu22.04

# Install Python and basic tools
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the student's requirements and install them
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Create the results directory (this will be mapped to the server)
RUN mkdir -p /app/results

# Set the working directory
WORKDIR /app
COPY . /app

# The command to run when the container starts
CMD ["python3", "train.py"]
