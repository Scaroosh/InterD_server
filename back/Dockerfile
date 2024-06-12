# Use a Python 3.12 slim image for a smaller footprint
FROM python:3.12-slim

# Create a working directory within the container
WORKDIR /app

# Copy the TA_Lib wheel file (assuming it's in your current directory)
COPY ./TA_Lib-0.4.29-cp312-cp312-win_amd64.whl /app

# # Install TA_Lib directly from the wheel file
RUN python3.12 -m pip install TA_Lib-0.4.29-cp312-cp312-win_amd64.whl

# Copy your requirements.txt file
COPY ./requirements.txt /app

# Install dependencies from requirements.txt
RUN python3.12 -m pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose port 8080 for the Flask app
EXPOSE 8080

# Set the working directory for the command (optional, but recommended for clarity)
ENV FLASK_APP=server.py

# Run the Flask app using the specified command
CMD ["python3.12", "-m", "flask", "--app", "server.py", "run", "-p", "8080"]