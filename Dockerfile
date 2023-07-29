# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container's working directory
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app files to the container's working directory
COPY main.py .

# Expose the port that Streamlit listens on (default is 8501)
EXPOSE 8501

# Command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "main.py"]
