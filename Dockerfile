# Base image: Python 3.9
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the required Python dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run tests inside the Docker container
CMD ["python", "-m", "pytest", "--headless"]